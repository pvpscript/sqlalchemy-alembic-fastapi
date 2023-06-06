from fastapi import Depends

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.models import document as document_model
from app.schemas import document as document_schema

from .base import BaseService

class DocumentService(BaseService[document_model.Document, document_schema.DocumentCreate, document_schema.DocumentUpdate]):
    def __init__(self, db_session: async_sessionmaker[AsyncSession]):
        super(DocumentService, self).__init__(document_model.Document, db_session)

def get_document_service(db_session: async_sessionmaker[AsyncSession] = Depends(get_session)) -> DocumentService:
    return DocumentService(db_session)
