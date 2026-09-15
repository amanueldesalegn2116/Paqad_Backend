from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from app.database import SessionLocal
from app.models import Project, Evidence, Discrepancy, VerificationRequest, VerificationResponse, Institution

load_dotenv()

router = APIRouter(prefix="/api/v1/chat", tags=["chat"])

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY", "")
NVIDIA_BASE_URL = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
NVIDIA_MODEL = os.getenv("NVIDIA_MODEL", "meta/llama-3.2-11b-vision-instruct")

BASE_SYSTEM_PROMPT = """You are Paqad AI, an assistant for a civic transparency and accountability platform that tracks public infrastructure projects in Ethiopia. You help users:
- Understand project statuses, budgets, and timelines
- Analyze discrepancies between official claims and evidence
- Explain verification processes
- Provide context about Ethiopian infrastructure development
- Answer questions about public accountability

Be factual, evidence-based, and neutral. Never make accusations. Use structured responses with headers and bullet points when helpful. Format responses in markdown.

Below is the LIVE DATA from the Paqad platform database. Use this data to answer user questions accurately:

"""


def build_data_context() -> str:
    """Query the database and build a context string with all platform data."""
    db = SessionLocal()
    try:
        institutions = db.query(Institution).all()
        inst_map = {inst.id: inst.name for inst in institutions}

        projects = db.query(Project).all()
        context = "## PROJECTS TRACKED\n"
        for p in projects:
            inst_name = inst_map.get(p.institution_id, "Unknown")
            context += (
                f"- **{p.title}** | Status: {p.status} | Location: {p.location}, {p.region} | "
                f"Institution: {inst_name} | "
                f"Promised Budget: {p.promised_budget:,.0f} ETB | Spent: {p.spent_budget:,.0f} ETB | "
                f"Progress: {p.progress_pct}% | "
                f"Promised: {p.promised_output} | Current: {p.current_output or 'N/A'} | "
                f"Deadline: {p.deadline}\n"
            )

        discrepancies = db.query(Discrepancy).all()
        proj_map = {p.id: p.title for p in projects}
        context += "\n## DISCREPANCIES DETECTED\n"
        for d in discrepancies:
            proj_title = proj_map.get(d.project_id, "Unknown Project")
            context += (
                f"- **Project: {proj_title}** | Official Claim: {d.official_claim} | "
                f"Reason Flagged: {d.reason_flagged} | "
                f"Verification Status: {d.verification_status} | Detected: {d.detected_at}\n"
            )

        evidence_items = db.query(Evidence).all()
        context += "\n## EVIDENCE COLLECTED\n"
        for ev in evidence_items:
            proj_title = proj_map.get(ev.project_id, "Unknown Project")
            context += (
                f"- **{ev.document_title}** (Project: {proj_title}) | "
                f"Source: {ev.source} ({ev.source_type}) | "
                f"Claim: {ev.extracted_claim} | "
                f"Status: {ev.evidence_status} | Date: {ev.evidence_date}\n"
            )

        vr_list = db.query(VerificationRequest).all()
        context += "\n## VERIFICATION REQUESTS\n"
        for vr in vr_list:
            proj_title = proj_map.get(vr.project_id, "Unknown Project")
            response = db.query(VerificationResponse).filter(
                VerificationResponse.request_id == vr.id
            ).first()
            resp_text = f" | Response: {response.response_text}" if response else " | No response yet"
            context += (
                f"- **Project: {proj_title}** | Info Requested: {vr.information_requested} | "
                f"State: {vr.current_state} | Requested: {vr.date_requested}{resp_text}\n"
            )

        total_budget = sum(p.promised_budget for p in projects)
        total_spent = sum(p.spent_budget for p in projects)
        context += "\n## SUMMARY STATS\n"
        context += f"- Total projects: {len(projects)}\n"
        context += f"- Total promised budget: {total_budget:,.0f} ETB\n"
        context += f"- Total spent budget: {total_spent:,.0f} ETB\n"
        context += f"- Discrepancies detected: {len(discrepancies)}\n"
        context += f"- Evidence items: {len(evidence_items)}\n"
        context += f"- Verification requests: {len(vr_list)}\n"

        return context
    finally:
        db.close()


def generate_local_fallback(user_query: str) -> str:
    """Generate a clean, informative response directly from live database data."""
    context = build_data_context()
    return (
        f"Here is the verified information from the Paqad platform database:\n\n"
        f"{context}\n\n"
        f"*Note: Answered using live platform database records.*"
    )


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[ChatMessage]
    stream: bool = True


def get_client() -> OpenAI:
    api_key = os.getenv("NVIDIA_API_KEY", "") or NVIDIA_API_KEY
    return OpenAI(base_url=NVIDIA_BASE_URL, api_key=api_key, timeout=20.0)


@router.post("")
def chat_completion(request: ChatRequest):
    api_key = os.getenv("NVIDIA_API_KEY", "") or NVIDIA_API_KEY
    if not api_key:
        raise HTTPException(status_code=500, detail="NVIDIA_API_KEY not configured")

    # Build system prompt with live database context
    data_context = build_data_context()
    system_prompt = BASE_SYSTEM_PROMPT + data_context

    messages = [{"role": "system", "content": system_prompt}]
    for msg in request.messages:
        messages.append({"role": msg.role, "content": msg.content})

    user_query = request.messages[-1].content if request.messages else ""

    if request.stream:
        def stream_response():
            try:
                client = get_client()
                model_name = os.getenv("NVIDIA_MODEL", NVIDIA_MODEL)
                response = client.chat.completions.create(
                    model=model_name,
                    messages=messages,
                    max_tokens=2048,
                    temperature=0.7,
                    stream=True,
                )

                has_content = False
                for chunk in response:
                    if not chunk.choices:
                        continue
                    delta = chunk.choices[0].delta
                    text = delta.content or getattr(delta, "reasoning_content", None)
                    if text:
                        has_content = True
                        payload = {"choices": [{"delta": {"content": text}}]}
                        yield f"data: {json.dumps(payload)}\n\n"

                if not has_content:
                    fallback = generate_local_fallback(user_query)
                    payload = {"choices": [{"delta": {"content": fallback}}]}
                    yield f"data: {json.dumps(payload)}\n\n"

                yield "data: [DONE]\n\n"

            except Exception as e:
                # If NVIDIA API times out or fails, gracefully return database data
                fallback = (
                    f"*(NVIDIA AI connection issue: {type(e).__name__}. Providing data from platform records:)*\n\n"
                    + generate_local_fallback(user_query)
                )
                payload = {"choices": [{"delta": {"content": fallback}}]}
                yield f"data: {json.dumps(payload)}\n\n"
                yield "data: [DONE]\n\n"

        return StreamingResponse(stream_response(), media_type="text/event-stream")
    else:
        try:
            client = get_client()
            model_name = os.getenv("NVIDIA_MODEL", NVIDIA_MODEL)
            resp = client.chat.completions.create(
                model=model_name,
                messages=messages,
                max_tokens=2048,
                temperature=0.7,
                stream=False,
            )
            return {
                "choices": [
                    {
                        "message": {
                            "role": "assistant",
                            "content": resp.choices[0].message.content,
                        }
                    }
                ]
            }
        except Exception as e:
            fallback = generate_local_fallback(user_query)
            return {
                "choices": [
                    {
                        "message": {
                            "role": "assistant",
                            "content": fallback,
                        }
                    }
                ]
            }
