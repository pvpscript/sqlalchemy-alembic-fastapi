from typing import Any, Optional, List
from uuid import UUID, uuid4
from datetime import datetime

from pydantic import BaseModel, Field

from app.schemas.document import Document
from app.schemas.asset import Asset


class UserBase(BaseModel):
    pass

class UserCreate(UserBase):
    id: Optional[UUID] = Field(default_factory=uuid4)
    age: int 
    first_name: str 
    last_name: str
    email: str
    bio: str

class UserUpdate(UserBase):
    email: Optional[str]
    bio: Optional[str]

class User(UserCreate):
    id: UUID
    platforms: List[Any] = []
    document: Optional[Document] = None
    assets: List[Asset] = []
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True

