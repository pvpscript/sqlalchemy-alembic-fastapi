import sqlalchemy as sa

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column 

from dataclasses import dataclass
from uuid import UUID
from datetime import datetime

from app.db.base_class import Base


@dataclass
class UserPlatformAssociation(Base):
    __tablename__ = 'user_platform_association'

    user_id: Mapped[UUID] = mapped_column(sa.UUID, sa.ForeignKey('user.id'), primary_key=True)
    platform_id: Mapped[UUID] = mapped_column(sa.UUID, sa.ForeignKey('platform.id'), primary_key=True)

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
