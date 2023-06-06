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
class Platform(Base):
    __tablename__ = 'platform'

    id: Mapped[UUID] = mapped_column(sa.UUID, nullable=False, primary_key=True)

    users: Mapped[List['User']] = relationship(
        secondary='user_platform_association', back_populates='platforms', lazy='selectin'
    )

    name: str = sa.Column(sa.String(255), nullable=False)
    description: str = sa.Column(sa.Text)

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
