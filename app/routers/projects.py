from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.models import Project, Institution, Evidence, Discrepancy, VerificationRequest
from app.schemas import ProjectRead, ProjectSummary

router = APIRouter(prefix="/api/v1/projects", tags=["projects"])


@router.get("", response_model=list[ProjectSummary])
def list_projects(
    status: Optional[str] = Query(None),
    region: Optional[str] = Query(None),
    institution_id: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(Project, Institution.name.label("institution_name")).join(
        Institution, Project.institution_id == Institution.id
    )

    if status:
        query = query.filter(Project.status == status)
    if region:
        query = query.filter(Project.region == region)
    if institution_id:
        query = query.filter(Project.institution_id == institution_id)
    if search:
        query = query.filter(Project.title.ilike(f"%{search}%"))

    results = query.order_by(Project.updated_at.desc()).all()

    return [
        ProjectSummary(
            id=p.id,
            title=p.title,
            institution_name=inst_name,
            location=p.location,
            region=p.region,
            promised_budget=p.promised_budget,
            status=p.status,
            progress_pct=p.progress_pct,
            deadline=p.deadline,
        )
        for p, inst_name in results
    ]


@router.get("/{project_id}", response_model=ProjectRead)
def get_project(project_id: str, db: Session = Depends(get_db)):
    result = (
        db.query(Project, Institution.name.label("institution_name"))
        .join(Institution, Project.institution_id == Institution.id)
        .filter(Project.id == project_id)
        .first()
    )
    if not result:
        raise HTTPException(status_code=404, detail="Project not found")

    p, inst_name = result
    return ProjectRead(
        id=p.id,
        institution_id=p.institution_id,
        institution_name=inst_name,
        title=p.title,
        description=p.description,
        location=p.location,
        region=p.region,
        latitude=p.latitude,
        longitude=p.longitude,
        promised_budget=p.promised_budget,
        spent_budget=p.spent_budget,
        promised_output=p.promised_output,
        current_output=p.current_output,
        announcement_date=p.announcement_date,
        deadline=p.deadline,
        status=p.status,
        progress_pct=p.progress_pct,
        created_at=p.created_at,
        updated_at=p.updated_at,
    )


@router.get("/{project_id}/timeline")
def get_project_timeline(project_id: str, db: Session = Depends(get_db)):
    """Get the accountability timeline for a project."""
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    evidence_items = (
        db.query(Evidence)
        .filter(Evidence.project_id == project_id)
        .order_by(Evidence.evidence_date)
        .all()
    )

    discrepancies = (
        db.query(Discrepancy)
        .filter(Discrepancy.project_id == project_id)
        .all()
    )

    ver_requests = (
        db.query(VerificationRequest)
        .filter(VerificationRequest.project_id == project_id)
        .order_by(VerificationRequest.date_requested)
        .all()
    )

    timeline = []

    # Announcement
    timeline.append({
        "date": str(project.announcement_date),
        "type": "announcement",
        "title": "Project Announced",
        "description": f"{project.title} announced with ETB {project.promised_budget:,.0f} budget.",
        "status": "completed",
    })

    # Evidence entries
    for ev in evidence_items:
        timeline.append({
            "date": str(ev.evidence_date),
            "type": "evidence",
            "title": ev.document_title,
            "description": ev.extracted_claim,
            "status": ev.evidence_status,
            "source_type": ev.source_type,
        })

    # Discrepancies
    for disc in discrepancies:
        timeline.append({
            "date": str(disc.detected_at.date() if disc.detected_at else ""),
            "type": "discrepancy",
            "title": "Discrepancy Detected",
            "description": disc.reason_flagged,
            "status": disc.verification_status,
        })

    # Verification requests
    for vr in ver_requests:
        timeline.append({
            "date": str(vr.date_requested),
            "type": "verification",
            "title": "Verification Requested",
            "description": vr.information_requested,
            "status": vr.current_state,
        })

    # Sort by date
    timeline.sort(key=lambda x: x["date"])

    return {"project_id": project_id, "timeline": timeline}
