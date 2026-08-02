from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,
    DateTime,
    Float,
)

from app.database.database import Base


class UserEvent(Base):

    __tablename__ = "user_events"


    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id = Column(
        Integer,
        nullable=False,
    )


    event_type = Column(
        String,
        nullable=False,
    )


    product_id = Column(
        Integer,
        nullable=True,
    )


    event_data = Column(
        JSON,
        nullable=True,
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

class ProductSnapshot(Base):

    __tablename__ = "product_snapshots"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    product_id = Column(
        Integer,
        unique=True,
        nullable=False,
    )

    name = Column(
        String,
        nullable=False,
    )

    category = Column(
        String,
        nullable=True,
    )

    brand = Column(
        String,
        nullable=True,
    )

    price = Column(
        Float,
        nullable=False,
    )