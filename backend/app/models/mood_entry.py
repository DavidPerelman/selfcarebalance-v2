from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import uuid
from .user import Base


class MoodEntry(Base):
    __tablename__ = "mood_entries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=True
    )  # אנונימי => user_id=None
    mood_score = Column(Integer, nullable=False)
    emotions = Column(
        String, nullable=True
    )  # נשמור כרשימת מחרוזות מופרדות בפסיקים, נחליף בעתיד ל־JSON
    notes = Column(String, nullable=True)
    is_anonymous = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))

    user = relationship("User", backref="mood_entries")
