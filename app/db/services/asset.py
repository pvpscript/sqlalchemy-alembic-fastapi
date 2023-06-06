from fastapi import Depends

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.models import asset as asset_model
from app.schemas import asset as asset_schema

from .base import BaseService

class AssetService(BaseService[asset_model.Asset, asset_schema.AssetCreate, asset_schema.AssetUpdate]):
    def __init__(self, db_session: async_sessionmaker[AsyncSession]):
        super(AssetService, self).__init__(asset_model.Asset, db_session)

def get_asset_service(db_session: async_sessionmaker[AsyncSession] = Depends(get_session)) -> AssetService:
    return AssetService(db_session)
