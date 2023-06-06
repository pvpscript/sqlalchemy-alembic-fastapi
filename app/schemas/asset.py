from typing import Optional, Any, List
from uuid import UUID, uuid4
from datetime import datetime

from pydantic import BaseModel, Field


class AssetBase(BaseModel):
    pass

class AssetCreate(AssetBase):
    id: Optional[UUID] = Field(default_factory=uuid4)
    user_id: Optional[UUID]
    name: str 
    price: int

class AssetUpdate(AssetBase):
    name: Optional[str]
    price: Optional[int]

class Asset(AssetCreate):
    id: UUID
    user: Any
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True
