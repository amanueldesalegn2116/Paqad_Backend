from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class EvidenceRead(BaseModel):
    id: str
    project_id: str
    project_title: str
    source: str
    source_type: str
    evidence_date: date
    document_title: str
    extracted_claim: str
    evidence_status: str
    file_url: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}


class EvidenceCreate(BaseModel):
    project_id: str
    source: str
    source_type: str
    evidence_date: date
    document_title: str
    extracted_claim: str
