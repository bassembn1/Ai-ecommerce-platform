from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,
    DateTime,
)

from datetime import datetime

from app.database.database import Base


class UserEvent(Base):

    __tablename__ = "user_events"

    id = Column(
        Integer,
        primary_key=True,
    )

    user_id = Column(
        Integer,
        nullable=False,
        index=True,
    )

    product_id = Column(
        Integer,
        nullable=False,
        index=True,
    )

    event_type = Column(
        String(50),
        nullable=False,
    )

    event_data = Column(
        JSON,
        nullable=True,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )