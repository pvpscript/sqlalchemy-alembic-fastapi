from typing import Any, Optional, List
from uuid import UUID, uuid4
from datetime import datetime

from pydantic import BaseModel, Field


class PlatformBase(BaseModel):
    pass

class PlatformCreate(PlatformBase):
    id: Optional[UUID] = Field(default_factory=uuid4)
    name: str 
    description: str

class PlatformUpdate(PlatformBase):
    description: Optional[str]

class Platform(PlatformCreate):
    id: UUID
    users: List[Any]
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True

