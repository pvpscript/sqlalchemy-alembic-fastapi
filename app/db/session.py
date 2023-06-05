import os

from functools import lru_cache

from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

PG_USER = os.getenv('PG_USER')
PG_PASS = os.getenv('PG_PASS')
PG_HOST = os.getenv('PG_HOST')
PG_NAME = os.getenv('PG_NAME')

DATABASE_URI=f'postgresql+asyncpg://{PG_USER}:{PG_PASS}@{PG_HOST}/{PG_NAME}'

engine = create_async_engine(DATABASE_URI, pool_pre_ping=True, echo=True)

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
