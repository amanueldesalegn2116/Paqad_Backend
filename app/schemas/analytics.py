from pydantic import BaseModel
from typing import List, Dict


class DashboardStats(BaseModel):
    total_projects: int
    total_promised_budget: float
    projects_monitoring: int
    verification_requests: int
    potential_discrepancies: int
    recent_activity: List[Dict]


class StatusDistribution(BaseModel):
    status: str
    count: int


class BudgetByRegion(BaseModel):
    region: str
    promised: float
    spent: float


class MonthlyTrend(BaseModel):
    month: str
    projects_added: int
    discrepancies_detected: int
    verifications_completed: int


class ChartData(BaseModel):
    status_distribution: List[StatusDistribution]
    budget_by_region: List[BudgetByRegion]
    monthly_trends: List[MonthlyTrend]
    completion_rate: float
    verification_rate: float
    response_rate: float
    avg_response_days: float
