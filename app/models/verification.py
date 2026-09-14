import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Date, ForeignKey, Text
from app.database import Base


class VerificationRequest(Base):
    __tablename__ = "verification_requests"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = Column(String, ForeignKey("projects.id"), nullable=False)
    discrepancy_id = Column(String, ForeignKey("discrepancies.id"), nullable=True)
    information_requested = Column(Text, nullable=False)
    date_requested = Column(Date, nullable=False)
    current_state = Column(String, nullable=False, default="Pending")
    # States: Pending, Acknowledged, Response Received, No Response, Closed
    created_at = Column(DateTime, default=datetime.utcnow)


class VerificationResponse(Base):
    __tablename__ = "verification_responses"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    request_id = Column(String, ForeignKey("verification_requests.id"), nullable=False)
    response_text = Column(Text, nullable=False)
    response_date = Column(Date, nullable=False)
    supporting_evidence_url = Column(String, nullable=True)
