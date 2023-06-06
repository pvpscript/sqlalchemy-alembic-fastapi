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
class Asset(Base):
    __tablename__ = 'asset'

    id: Mapped[UUID] = mapped_column(sa.UUID, nullable=False, primary_key=True)
    user_id: Mapped[UUID] = mapped_column(sa.ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='assets', lazy='selectin')

    name: str = sa.Column(sa.String(255), nullable=False, unique=True)
    price: int = sa.Column(sa.Integer, nullable=False)

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
