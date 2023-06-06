from typing import Optional, List
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class UserPlatformBase(BaseModel):
    pass

class UserPlatformCreate(UserPlatformBase):
    user_id: UUID
    platform_id: UUID

class UserPlatform(UserPlatformCreate):
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True
