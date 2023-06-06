from fastapi import Depends

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.models import user_platform_association as user_platform_association_model
from app.schemas import user_platform as user_platform_schema

from .base import BaseService

class UserPlatformAssociationService(
    BaseService[user_platform_association_model.UserPlatformAssociation,
                user_platform_schema.UserPlatformCreate,
                None]
):
    def __init__(self, db_session: async_sessionmaker[AsyncSession]):
        super(UserPlatformAssociationService, self).__init__(
            user_platform_association_model.UserPlatformAssociation, db_session
        )

def get_user_platform_association_service(
    db_session: async_sessionmaker[AsyncSession] = Depends(get_session)
) -> UserPlatformAssociationService:
    return UserPlatformAssociationService(db_session)
