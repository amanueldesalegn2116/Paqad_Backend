"""Analytics service for computing dashboard and chart data."""

from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Project, Evidence, Discrepancy, VerificationRequest, VerificationResponse, PublicReport


def get_dashboard_stats(db: Session) -> dict:
    total_projects = db.query(Project).count()
    total_budget = db.query(func.sum(Project.promised_budget)).scalar() or 0
    monitoring = db.query(Project).filter(Project.status == "Monitoring").count()
    ver_requests = db.query(VerificationRequest).count()
    discrepancies = db.query(Discrepancy).count()

    # Recent activity: last 10 evidence/reports by date
    recent_evidence = (
        db.query(Evidence)
        .order_by(Evidence.created_at.desc())
        .limit(5)
        .all()
    )
    recent_reports = (
        db.query(PublicReport)
        .order_by(PublicReport.created_at.desc())
        .limit(5)
        .all()
    )

    recent_activity = []
    for ev in recent_evidence:
        project = db.query(Project).filter(Project.id == ev.project_id).first()
        recent_activity.append({
            "type": "evidence",
            "title": ev.document_title,
            "project_title": project.title if project else "Unknown",
            "date": str(ev.evidence_date),
            "source_type": ev.source_type,
        })
    for rp in recent_reports:
        project = db.query(Project).filter(Project.id == rp.project_id).first()
        recent_activity.append({
            "type": "report",
            "title": f"Public Report: {rp.description[:60]}...",
            "project_title": project.title if project else "Unknown",
            "date": str(rp.report_date),
            "source_type": "citizen_report",
        })

    recent_activity.sort(key=lambda x: x["date"], reverse=True)

    return {
        "total_projects": total_projects,
        "total_promised_budget": total_budget,
        "projects_monitoring": monitoring,
        "verification_requests": ver_requests,
        "potential_discrepancies": discrepancies,
        "recent_activity": recent_activity[:10],
    }


def get_chart_data(db: Session) -> dict:
    # Status distribution
    statuses = (
        db.query(Project.status, func.count(Project.id))
        .group_by(Project.status)
        .all()
    )
    status_distribution = [
        {"status": s, "count": c} for s, c in statuses
    ]

    # Budget by region
    regions = (
        db.query(
            Project.region,
            func.sum(Project.promised_budget),
            func.sum(Project.spent_budget),
        )
        .group_by(Project.region)
        .all()
    )
    budget_by_region = [
        {"region": r, "promised": p or 0, "spent": s or 0}
        for r, p, s in regions
    ]

    # Completion rate (verified / total)
    verified = db.query(Project).filter(Project.status == "Verified").count()
    total = db.query(Project).count()
    completion_rate = (verified / total * 100) if total > 0 else 0

    # Verification rate
    total_requests = db.query(VerificationRequest).count()
    responded = db.query(VerificationResponse).count()
    verification_rate = (responded / total_requests * 100) if total_requests > 0 else 0

    # Response rate
    non_pending = db.query(VerificationRequest).filter(
        VerificationRequest.current_state != "Pending"
    ).count()
    response_rate = (non_pending / total_requests * 100) if total_requests > 0 else 0

    # Monthly trends (mock static data for prototype)
    monthly_trends = [
        {"month": "2025-01", "projects_added": 1, "discrepancies_detected": 0, "verifications_completed": 0},
        {"month": "2025-03", "projects_added": 2, "discrepancies_detected": 1, "verifications_completed": 0},
        {"month": "2025-05", "projects_added": 1, "discrepancies_detected": 1, "verifications_completed": 1},
        {"month": "2025-07", "projects_added": 2, "discrepancies_detected": 2, "verifications_completed": 0},
        {"month": "2025-09", "projects_added": 1, "discrepancies_detected": 1, "verifications_completed": 1},
        {"month": "2025-11", "projects_added": 2, "discrepancies_detected": 1, "verifications_completed": 0},
        {"month": "2026-01", "projects_added": 1, "discrepancies_detected": 0, "verifications_completed": 1},
        {"month": "2026-03", "projects_added": 1, "discrepancies_detected": 1, "verifications_completed": 0},
        {"month": "2026-05", "projects_added": 0, "discrepancies_detected": 0, "verifications_completed": 1},
        {"month": "2026-07", "projects_added": 1, "discrepancies_detected": 1, "verifications_completed": 0},
        {"month": "2026-09", "projects_added": 1, "discrepancies_detected": 0, "verifications_completed": 0},
    ]

    return {
        "status_distribution": status_distribution,
        "budget_by_region": budget_by_region,
        "monthly_trends": monthly_trends,
        "completion_rate": round(completion_rate, 1),
        "verification_rate": round(verification_rate, 1),
        "response_rate": round(response_rate, 1),
        "avg_response_days": 18.5,  # Mock average
    }
