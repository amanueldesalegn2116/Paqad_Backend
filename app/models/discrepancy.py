import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from app.database import Base


class Discrepancy(Base):
    __tablename__ = "discrepancies"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = Column(String, ForeignKey("projects.id"), nullable=False)
    official_claim = Column(Text, nullable=False)
    supporting_evidence_id = Column(String, ForeignKey("evidence.id"), nullable=True)
    conflicting_evidence_id = Column(String, ForeignKey("evidence.id"), nullable=True)
    reason_flagged = Column(Text, nullable=False)
    verification_status = Column(String, nullable=False, default="Pending")
    # Status: Pending, Under Review, Resolved, Unresolved
    detected_at = Column(DateTime, default=datetime.utcnow)
