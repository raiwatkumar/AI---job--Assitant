from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from .db import Base


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(120), nullable=False)
    role = Column(String(120), nullable=False)
    link = Column(String(500), nullable=True)
    status = Column(String(30), nullable=False, default="Saved")
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
