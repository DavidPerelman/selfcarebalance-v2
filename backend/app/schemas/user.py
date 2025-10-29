from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime


class UserOut(BaseModel):
    id: UUID
    email: EmailStr
    full_name: str | None
    created_at: datetime

    class Config:
        orm_mode = True
