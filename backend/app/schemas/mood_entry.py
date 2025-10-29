from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID
from datetime import datetime


class MoodEntryIn(BaseModel):
    mood_score: int = Field(..., ge=1, le=10)
    emotions: Optional[List[str]] = []
    notes: Optional[str] = None
    is_anonymous: Optional[bool] = False


class MoodEntryOut(MoodEntryIn):
    id: UUID
    timestamp: datetime

    class Config:
        orm_mode = True
