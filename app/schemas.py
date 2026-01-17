from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional


class ApplicationCreate(BaseModel):
    company: str = Field(..., min_length=2, max_length=120)
    role: str = Field(..., min_length=2, max_length=120)
    link: Optional[str] = Field(None, max_length=500)
    status: str = Field("Saved", max_length=30)
    notes: Optional[str] = None


class ApplicationOut(BaseModel):
    id: int
    company: str
    role: str
    link: Optional[str]
    status: str
    notes: Optional[str]
    created_at: datetime

    # Pydantic v2 configuration: allow loading from ORM objects
    model_config = ConfigDict(from_attributes=True)
