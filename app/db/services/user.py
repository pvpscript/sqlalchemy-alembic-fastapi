from fastapi import Depends

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import session
from app.models import user as user_model
from app.schemas import user as user_schema

from .base import BaseService

class UserService(BaseService[user_model.User, user_schema.UserCreate, user_schema.UserUpdate]):
    def __init__(self, db_session: async_sessionmaker[AsyncSession]):
        super(UserService, self).__init__(user_model.User, db_session)

def get_user_service(db_session: async_sessionmaker[AsyncSession] = Depends(session.get_session)) -> UserService:
    return UserService(db_session)
