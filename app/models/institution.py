import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from app.database import Base


class Institution(Base):
    __tablename__ = "institutions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # federal, regional, municipal, agency
    region = Column(String, nullable=True)
    logo_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
