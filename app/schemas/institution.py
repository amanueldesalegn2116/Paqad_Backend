from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class InstitutionRead(BaseModel):
    id: str
    name: str
    type: str
    region: Optional[str] = None
    logo_url: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}
