from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.models import Discrepancy, Project, Evidence
from app.schemas import DiscrepancyRead

router = APIRouter(prefix="/api/v1/discrepancies", tags=["discrepancies"])


@router.get("", response_model=list[DiscrepancyRead])
def list_discrepancies(
    project_id: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(Discrepancy)

    if project_id:
        query = query.filter(Discrepancy.project_id == project_id)
    if status:
        query = query.filter(Discrepancy.verification_status == status)

    discs = query.order_by(Discrepancy.detected_at.desc()).all()

    results = []
    for d in discs:
        project = db.query(Project).filter(Project.id == d.project_id).first()
        sup_ev = db.query(Evidence).filter(Evidence.id == d.supporting_evidence_id).first() if d.supporting_evidence_id else None
        con_ev = db.query(Evidence).filter(Evidence.id == d.conflicting_evidence_id).first() if d.conflicting_evidence_id else None

        results.append(DiscrepancyRead(
            id=d.id,
            project_id=d.project_id,
            project_title=project.title if project else "Unknown",
            official_claim=d.official_claim,
            supporting_evidence_id=d.supporting_evidence_id,
            supporting_evidence_summary=sup_ev.extracted_claim if sup_ev else None,
            conflicting_evidence_id=d.conflicting_evidence_id,
            conflicting_evidence_summary=con_ev.extracted_claim if con_ev else None,
            reason_flagged=d.reason_flagged,
            verification_status=d.verification_status,
            detected_at=d.detected_at,
        ))

    return results


@router.get("/{discrepancy_id}", response_model=DiscrepancyRead)
def get_discrepancy(discrepancy_id: str, db: Session = Depends(get_db)):
    d = db.query(Discrepancy).filter(Discrepancy.id == discrepancy_id).first()
    if not d:
        raise HTTPException(status_code=404, detail="Discrepancy not found")

    project = db.query(Project).filter(Project.id == d.project_id).first()
    sup_ev = db.query(Evidence).filter(Evidence.id == d.supporting_evidence_id).first() if d.supporting_evidence_id else None
    con_ev = db.query(Evidence).filter(Evidence.id == d.conflicting_evidence_id).first() if d.conflicting_evidence_id else None

    return DiscrepancyRead(
        id=d.id,
        project_id=d.project_id,
        project_title=project.title if project else "Unknown",
        official_claim=d.official_claim,
        supporting_evidence_id=d.supporting_evidence_id,
        supporting_evidence_summary=sup_ev.extracted_claim if sup_ev else None,
        conflicting_evidence_id=d.conflicting_evidence_id,
        conflicting_evidence_summary=con_ev.extracted_claim if con_ev else None,
        reason_flagged=d.reason_flagged,
        verification_status=d.verification_status,
        detected_at=d.detected_at,
    )
