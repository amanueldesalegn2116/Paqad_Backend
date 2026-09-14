from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class DiscrepancyRead(BaseModel):
    id: str
    project_id: str
    project_title: str
    official_claim: str
    supporting_evidence_id: Optional[str] = None
    supporting_evidence_summary: Optional[str] = None
    conflicting_evidence_id: Optional[str] = None
    conflicting_evidence_summary: Optional[str] = None
    reason_flagged: str
    verification_status: str
    detected_at: datetime

    model_config = {"from_attributes": True}
