import os

from asyncio import current_task

from functools import lru_cache

from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import async_scoped_session
from sqlalchemy.ext.asyncio import AsyncSession

from app.resources.config import Config


@lru_cache
def create_session() -> AsyncSession:
    engine = create_async_engine(Config.DATABASE_URI, pool_pre_ping=True, echo=True)
    session = async_sessionmaker(autocommit=False,
                                 autoflush=False,
                                 expire_on_commit=False,
                                 bind=engine)

    return async_scoped_session(session, scopefunc=current_task)

async def get_session() -> Any:
    AsyncSession = create_session()
    async with AsyncSession() as async_session:
        yield async_session
