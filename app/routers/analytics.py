from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import DashboardStats, ChartData
from app.services.analytics import get_dashboard_stats, get_chart_data

router = APIRouter(prefix="/api/v1/analytics", tags=["analytics"])


@router.get("/dashboard", response_model=DashboardStats)
def dashboard(db: Session = Depends(get_db)):
    return get_dashboard_stats(db)


@router.get("/charts", response_model=ChartData)
def charts(db: Session = Depends(get_db)):
    return get_chart_data(db)
