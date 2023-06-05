from typing import Optional, List
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel

#from app.schemas.platform import PlatformBase

class UserBase(BaseModel):
    pass

class UserCreate(UserBase):
    #platforms: List[PlatformBase]
    platforms: List[BaseModel]
    age: int 
    first_name: str 
    last_name: str
    email: str
    bio: str

class UserUpdate(UserBase):
    #platforms: List[PlatformBase]
    platforms: List[BaseModel]
    email: Optional[str]
    bio: Optional[str]

class User(UserCreate):
    id: UUID
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True
