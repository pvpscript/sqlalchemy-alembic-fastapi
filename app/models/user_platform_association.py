import sqlalchemy as sa

from app.db.base_class import Base

association_table = sa.Table(
    'user_platform_association',
    Base.metadata,
    sa.Column(
        'user_id',
        sa.ForeignKey('user.id'),
        primary_key=True,
    ),
    sa.Column(
        'platform_id',
        sa.ForeignKey('platform.id'),
        primary_key=True,
    ),
)

