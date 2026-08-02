from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    JSON,
)

from sqlalchemy.sql import func

from app.database.base import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True,
    )

    product_id = Column(
        Integer,
        nullable=True,
    )

    event_type = Column(
        String,
        nullable=False,
    )

    event_data = Column(JSON, nullable=True)

    created_at = Column(
        DateTime,
        server_default=func.now(),
    )