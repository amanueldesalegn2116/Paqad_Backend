import uuid
from datetime import date as date_type
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import VerificationRequest, VerificationResponse, Project
from app.schemas import VerificationRequestRead, VerificationRequestCreate, VerificationResponseRead

router = APIRouter(prefix="/api/v1/verification-requests", tags=["verification"])


@router.get("", response_model=list[VerificationRequestRead])
def list_verification_requests(db: Session = Depends(get_db)):
    vrs = db.query(VerificationRequest).order_by(VerificationRequest.date_requested.desc()).all()

    results = []
    for vr in vrs:
        project = db.query(Project).filter(Project.id == vr.project_id).first()
        response = db.query(VerificationResponse).filter(
            VerificationResponse.request_id == vr.id
        ).first()

        resp_data = None
        if response:
            resp_data = VerificationResponseRead(
                id=response.id,
                request_id=response.request_id,
                response_text=response.response_text,
                response_date=response.response_date,
                supporting_evidence_url=response.supporting_evidence_url,
            )

        results.append(VerificationRequestRead(
            id=vr.id,
            project_id=vr.project_id,
            project_title=project.title if project else "Unknown",
            discrepancy_id=vr.discrepancy_id,
            information_requested=vr.information_requested,
            date_requested=vr.date_requested,
            current_state=vr.current_state,
            response=resp_data,
            created_at=vr.created_at,
        ))

    return results


@router.post("", response_model=VerificationRequestRead, status_code=201)
def create_verification_request(
    data: VerificationRequestCreate,
    db: Session = Depends(get_db),
):
    project = db.query(Project).filter(Project.id == data.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    vr = VerificationRequest(
        id=str(uuid.uuid4()),
        project_id=data.project_id,
        discrepancy_id=data.discrepancy_id,
        information_requested=data.information_requested,
        date_requested=data.date_requested,
        current_state="Pending",
    )
    db.add(vr)
    db.commit()
    db.refresh(vr)

    return VerificationRequestRead(
        id=vr.id,
        project_id=vr.project_id,
        project_title=project.title,
        discrepancy_id=vr.discrepancy_id,
        information_requested=vr.information_requested,
        date_requested=vr.date_requested,
        current_state=vr.current_state,
        response=None,
        created_at=vr.created_at,
    )
