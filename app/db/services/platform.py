from fastapi import Depends

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.models import platform as platform_model
from app.schemas import platform as platform_schema

from .base import BaseService

class PlatformService(BaseService[platform_model.Platform, platform_schema.PlatformCreate, platform_schema.PlatformUpdate]):
    def __init__(self, db_session: async_sessionmaker[AsyncSession]):
        super(PlatformService, self).__init__(platform_model.Platform, db_session)

def get_platform_service(db_session: async_sessionmaker[AsyncSession] = Depends(get_session)) -> PlatformService:
    return PlatformService(db_session)
