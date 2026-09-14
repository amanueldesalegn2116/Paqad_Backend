import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Float, Date, ForeignKey, Text
from app.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    institution_id = Column(String, ForeignKey("institutions.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    location = Column(String, nullable=False)
    region = Column(String, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    promised_budget = Column(Float, nullable=False)
    spent_budget = Column(Float, default=0.0)
    promised_output = Column(String, nullable=False)
    current_output = Column(String, nullable=True)
    announcement_date = Column(Date, nullable=False)
    deadline = Column(Date, nullable=False)
    status = Column(String, nullable=False, default="Reported")
    # Status values: Reported, Documented, Monitoring,
    # Verification Requested, Partially Verified, Verified,
    # Conflicting Evidence, Unresolved
    progress_pct = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
