from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class PublicReportRead(BaseModel):
    id: str
    project_id: str
    project_title: str
    description: str
    photo_url: Optional[str] = None
    location: Optional[str] = None
    report_date: date
    status: str
    reporter_name: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}


class PublicReportCreate(BaseModel):
    project_id: str
    description: str
    photo_url: Optional[str] = None
    location: Optional[str] = None
    report_date: date
    reporter_name: Optional[str] = None
