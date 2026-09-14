import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import PublicReport, Project
from app.schemas import PublicReportRead, PublicReportCreate

router = APIRouter(prefix="/api/v1/reports", tags=["reports"])


@router.get("", response_model=list[PublicReportRead])
def list_reports(db: Session = Depends(get_db)):
    reports = db.query(PublicReport).order_by(PublicReport.created_at.desc()).all()

    results = []
    for r in reports:
        project = db.query(Project).filter(Project.id == r.project_id).first()
        results.append(PublicReportRead(
            id=r.id,
            project_id=r.project_id,
            project_title=project.title if project else "Unknown",
            description=r.description,
            photo_url=r.photo_url,
            location=r.location,
            report_date=r.report_date,
            status=r.status,
            reporter_name=r.reporter_name,
            created_at=r.created_at,
        ))
    return results


@router.post("", response_model=PublicReportRead, status_code=201)
def create_report(data: PublicReportCreate, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == data.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    report = PublicReport(
        id=str(uuid.uuid4()),
        project_id=data.project_id,
        description=data.description,
        photo_url=data.photo_url,
        location=data.location,
        report_date=data.report_date,
        reporter_name=data.reporter_name,
        status="Submitted",
    )
    db.add(report)
    db.commit()
    db.refresh(report)

    return PublicReportRead(
        id=report.id,
        project_id=report.project_id,
        project_title=project.title,
        description=report.description,
        photo_url=report.photo_url,
        location=report.location,
        report_date=report.report_date,
        status=report.status,
        reporter_name=report.reporter_name,
        created_at=report.created_at,
    )
