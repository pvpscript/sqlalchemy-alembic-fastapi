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
class User(Base):
    __tablename__ = 'user'

    id: Mapped[UUID] = mapped_column(sa.UUID, nullable=False, primary_key=True)

    platforms: Mapped[List['Platform']] = relationship(
        secondary='user_platform_association', back_populates='users', lazy='selectin',
    )
    document: Mapped['Document'] = relationship(back_populates='user', lazy='selectin')
    assets: Mapped[List['Asset']] = relationship(back_populates='user', lazy='selectin')

    age: int = sa.Column(sa.Integer, nullable=False)
    first_name: str = sa.Column(sa.String(255), nullable=False)
    last_name: str = sa.Column(sa.String(255), nullable=False)
    email: str = sa.Column(sa.String(255), nullable=False, unique=True)
    bio: str = sa.Column(sa.Text)

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
