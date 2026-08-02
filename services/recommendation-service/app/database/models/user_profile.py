from sqlalchemy import (
    Column,
    Integer,
    JSON,
)

from app.database.database import Base


class UserProfile(Base):

    __tablename__ = "user_profiles"

    user_id = Column(
        Integer,
        primary_key=True,
    )

    preferences = Column(
        JSON,
        nullable=True,
    )