import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Date, ForeignKey, Text
from app.database import Base


class Evidence(Base):
    __tablename__ = "evidence"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = Column(String, ForeignKey("projects.id"), nullable=False)
    source = Column(String, nullable=False)  # e.g., "Ethiopian Roads Authority"
    source_type = Column(String, nullable=False)
    # Source types: government_announcement, progress_report, budget_report,
    # citizen_report, media_report, photo_evidence, official_document, audit_report
    evidence_date = Column(Date, nullable=False)
    document_title = Column(String, nullable=False)
    extracted_claim = Column(Text, nullable=False)
    evidence_status = Column(String, nullable=False, default="Pending Review")
    # Status: Pending Review, Reviewed, Corroborated, Contested, Retracted
    file_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
