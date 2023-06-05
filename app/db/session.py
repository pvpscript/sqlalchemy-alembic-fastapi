import os

from functools import lru_cache

from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from app.resources.config import Config

engine = create_async_engine(Config.DATABASE_URI, pool_pre_ping=True, echo=True)

@lru_cache
def create_session() -> AsyncSession:
    return async_sessionmaker(autocommit=False,
                              autoflush=False,
                              expire_on_commit=False,
                              bind=engine)

def get_session() -> Any:
    AsyncSession = create_session()
    try:
        yield AsyncSession
    finally:
        #AsyncSession.remove()
        pass
