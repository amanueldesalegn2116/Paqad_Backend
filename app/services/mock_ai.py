"""
Mock AI service layer.
In production, this would be replaced with actual NLP / document ingestion.
For the prototype, it uses deterministic logic.
"""

from typing import Optional


def analyze_evidence_consistency(
    official_claim: str,
    evidence_claim: str,
) -> dict:
    """
    Mock AI analysis comparing an official claim against evidence.
    Returns a consistency assessment.

    In production, this would use an LLM or NLP pipeline to perform
    semantic comparison between claims and evidence.
    """
    # Simple deterministic mock: check for keyword overlaps
    official_lower = official_claim.lower()
    evidence_lower = evidence_claim.lower()

    # Look for contradiction indicators
    contradiction_words = [
        "only", "incomplete", "defect", "not", "no ", "stopped",
        "untreated", "impassable", "behind schedule", "shortfall",
    ]

    has_contradiction = any(w in evidence_lower for w in contradiction_words)

    if has_contradiction:
        return {
            "consistency_score": 0.35,
            "assessment": "Potential discrepancy detected",
            "confidence": 0.7,
            "recommendation": "Verification recommended",
        }

    return {
        "consistency_score": 0.85,
        "assessment": "Claims appear consistent",
        "confidence": 0.8,
        "recommendation": "Continue monitoring",
    }


def extract_claims_from_document(document_text: str) -> list[dict]:
    """
    Mock document claim extraction.
    In production, this would parse PDFs, extract text, and identify
    specific factual claims using NLP.
    """
    # For prototype, return the full text as a single claim
    return [
        {
            "claim_text": document_text,
            "confidence": 0.9,
            "claim_type": "factual_statement",
        }
    ]


def calculate_project_risk_score(
    progress_pct: float,
    budget_ratio: float,
    days_to_deadline: int,
    discrepancy_count: int,
) -> dict:
    """
    Mock risk assessment for a project.
    In production, this would use ML models trained on project data.
    """
    risk_score = 0.0

    # Progress risk
    if progress_pct < 30:
        risk_score += 0.3
    elif progress_pct < 60:
        risk_score += 0.15

    # Budget risk
    if budget_ratio > 0.9:
        risk_score += 0.2
    elif budget_ratio > 0.7:
        risk_score += 0.1

    # Timeline risk
    if days_to_deadline < 180 and progress_pct < 70:
        risk_score += 0.3
    elif days_to_deadline < 365 and progress_pct < 50:
        risk_score += 0.2

    # Discrepancy risk
    risk_score += min(discrepancy_count * 0.1, 0.3)

    risk_score = min(risk_score, 1.0)

    if risk_score > 0.7:
        risk_level = "High"
    elif risk_score > 0.4:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "risk_score": round(risk_score, 2),
        "risk_level": risk_level,
    }
