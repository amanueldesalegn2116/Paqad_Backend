from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class ProjectSummary(BaseModel):
    id: str
    title: str
    institution_name: str
    location: str
    region: str
    promised_budget: float
    status: str
    progress_pct: float
    deadline: date

    model_config = {"from_attributes": True}


class ProjectRead(BaseModel):
    id: str
    institution_id: str
    institution_name: str
    title: str
    description: Optional[str] = None
    location: str
    region: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    promised_budget: float
    spent_budget: float
    promised_output: str
    current_output: Optional[str] = None
    announcement_date: date
    deadline: date
    status: str
    progress_pct: float
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ProjectCreate(BaseModel):
    institution_id: str
    title: str
    description: Optional[str] = None
    location: str
    region: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    promised_budget: float
    promised_output: str
    announcement_date: date
    deadline: date
