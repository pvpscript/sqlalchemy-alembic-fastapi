import sqlalchemy as sa

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column 
from sqlalchemy.orm import relationship

from dataclasses import dataclass

from typing import List
from datetime import datetime
from uuid import uuid4, UUID

from app.db.base_class import Base

#from app.models.platform import Platform

from app.models.user_platform_association import association_table

@dataclass
class User(Base):
    __tablename__ = 'user'

    id: Mapped[UUID] = mapped_column(sa.UUID, nullable=False, primary_key=True, default=uuid4())

    platforms: Mapped[List['Platform']] = relationship(
        secondary=association_table, back_populates='users'
    )

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
