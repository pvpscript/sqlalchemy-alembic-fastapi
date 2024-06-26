import sqlalchemy as sa

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column 
from sqlalchemy.orm import relationship

from dataclasses import dataclass

from typing import List
from datetime import datetime
from uuid import uuid4, UUID

from app.db.base_class import Base


@dataclass
class Document(Base):
    __tablename__ = 'document'

    id: Mapped[UUID] = mapped_column(sa.UUID, nullable=False, primary_key=True)
    user_id: Mapped[UUID] = mapped_column(sa.ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='document', lazy='selectin')

    value: str = sa.Column(sa.String(20), nullable=False, unique=True)

    created_at: datetime = sa.Column(
        sa.TIMESTAMP(timezone=True),
        nullable=False,
        server_default=sa.func.now()
    )
    modified_at: datetime = sa.Column(
        sa.TIMESTAMP(timezone=True),
        nullable=False,
        server_default=sa.func.now()
    )
