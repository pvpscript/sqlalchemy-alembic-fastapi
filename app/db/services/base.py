from typing import Any, Generic, List, Optional, Type, TypeVar

from pydantic import BaseModel

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType], db_session: async_sessionmaker[AsyncSession]):
        self._model = model
        self._db_session = db_session

    async def _find_by_id(self, id: Any) -> Optional[ModelType]:
        stmt = select(self._model).where(self._model.id == id)
        result = await self._db_session.execute(stmt)

        return result.unique().scalars().one()

    async def find_by_id(self, id: Any) -> Optional[ModelType]:
        return await self._find_by_id(id)

    async def list(self) -> List[ModelType]:
        stmt = select(self._model)
        result = await self._db_session.execute(stmt)

        return result.scalars().all()

    async def save(self, obj: CreateSchemaType) -> ModelType:
        stmt = (
            insert(self._model)
                .values(**obj.dict())
                .returning(self._model)
        )

        result = await self._db_session.execute(stmt)

        return result.unique().scalars().one()

    async def update(self, id: Any, obj: UpdateSchemaType) -> Optional[ModelType]:
        stmt = (
            update(self._model)
                .values(**obj.dict(exclude_unset=True))
                .where(self._model.id == id)
                .returning(self._model)
        )

        result = await self._db_session.execute(stmt)

        return result.unique().scalars().one_or_none()

    async def delete(self, id: Any) -> None:
        stmt = delete(self._model).where(self._model.id == id)

        await self._db_session.execute(stmt)
