from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(String)

    email = Column(
        String,
        unique=True,
        index=True
    )

    hashed_password = Column(String)

    role = Column(
        String,
        default="customer",
        nullable=False,
    )