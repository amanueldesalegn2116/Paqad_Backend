from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class VerificationRequestRead(BaseModel):
    id: str
    project_id: str
    project_title: str
    discrepancy_id: Optional[str] = None
    information_requested: str
    date_requested: date
    current_state: str
    response: Optional["VerificationResponseRead"] = None
    created_at: datetime

    model_config = {"from_attributes": True}


class VerificationRequestCreate(BaseModel):
    project_id: str
    discrepancy_id: Optional[str] = None
    information_requested: str
    date_requested: date


class VerificationResponseRead(BaseModel):
    id: str
    request_id: str
    response_text: str
    response_date: date
    supporting_evidence_url: Optional[str] = None

    model_config = {"from_attributes": True}
