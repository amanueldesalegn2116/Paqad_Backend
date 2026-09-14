import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Date, ForeignKey, Text
from app.database import Base


class PublicReport(Base):
    __tablename__ = "public_reports"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = Column(String, ForeignKey("projects.id"), nullable=False)
    description = Column(Text, nullable=False)
    photo_url = Column(String, nullable=True)
    location = Column(String, nullable=True)
    report_date = Column(Date, nullable=False)
    status = Column(String, nullable=False, default="Submitted")
    # Status: Submitted, Under Review, Acknowledged, Incorporated, Dismissed
    reporter_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
