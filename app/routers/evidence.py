from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.models import Evidence, Project
from app.schemas import EvidenceRead

router = APIRouter(prefix="/api/v1/evidence", tags=["evidence"])


@router.get("", response_model=list[EvidenceRead])
def list_evidence(
    project_id: Optional[str] = Query(None),
    source_type: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(Evidence, Project.title.label("project_title")).join(
        Project, Evidence.project_id == Project.id
    )

    if project_id:
        query = query.filter(Evidence.project_id == project_id)
    if source_type:
        query = query.filter(Evidence.source_type == source_type)
    if status:
        query = query.filter(Evidence.evidence_status == status)
    if search:
        query = query.filter(
            Evidence.document_title.ilike(f"%{search}%")
            | Evidence.extracted_claim.ilike(f"%{search}%")
        )

    results = query.order_by(Evidence.evidence_date.desc()).all()

    return [
        EvidenceRead(
            id=ev.id,
            project_id=ev.project_id,
            project_title=proj_title,
            source=ev.source,
            source_type=ev.source_type,
            evidence_date=ev.evidence_date,
            document_title=ev.document_title,
            extracted_claim=ev.extracted_claim,
            evidence_status=ev.evidence_status,
            file_url=ev.file_url,
            created_at=ev.created_at,
        )
        for ev, proj_title in results
    ]


@router.get("/{evidence_id}", response_model=EvidenceRead)
def get_evidence(evidence_id: str, db: Session = Depends(get_db)):
    result = (
        db.query(Evidence, Project.title.label("project_title"))
        .join(Project, Evidence.project_id == Project.id)
        .filter(Evidence.id == evidence_id)
        .first()
    )
    if not result:
        raise HTTPException(status_code=404, detail="Evidence not found")

    ev, proj_title = result
    return EvidenceRead(
        id=ev.id,
        project_id=ev.project_id,
        project_title=proj_title,
        source=ev.source,
        source_type=ev.source_type,
        evidence_date=ev.evidence_date,
        document_title=ev.document_title,
        extracted_claim=ev.extracted_claim,
        evidence_status=ev.evidence_status,
        file_url=ev.file_url,
        created_at=ev.created_at,
    )
