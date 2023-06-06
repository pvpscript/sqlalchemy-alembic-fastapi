from typing import Optional, Any, List
from uuid import UUID, uuid4
from datetime import datetime

from pydantic import BaseModel, Field


class DocumentBase(BaseModel):
    pass

class DocumentCreate(DocumentBase):
    id: Optional[UUID] = Field(default_factory=uuid4)
    user_id: Optional[UUID]
    value: str 

class DocumentUpdate(DocumentBase):
    value: str

class Document(DocumentCreate):
    id: UUID
    user: Any
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True
