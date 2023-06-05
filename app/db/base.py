# Base class, used by alembic
from app.db.base_class import Base

# Model classes
from app.models.user import User
from app.models.platform import Platform
from app.models.user_platform_association import association_table
