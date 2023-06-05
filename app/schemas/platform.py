from typing import Optional, List
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel

#from app.schemas.user import UserBase


class PlatformBase(BaseModel):
    pass

class PlatformCreate(PlatformBase):
    #users: List[UserBase]
    users: List[BaseModel]
    name: str 
    description: str

class PlatformUpdate(PlatformBase):
    #users: List[UserBase]
    users: List[BaseModel]
    description: Optional[str]

class Platform(PlatformCreate):
    id: UUID
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True
