from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    JSON,
    DateTime,
)

from app.database.database import Base


class ProductEmbedding(Base):

    __tablename__ = "product_embeddings"

    id = Column(
        Integer,
        primary_key=True,
    )

    product_id = Column(
        Integer,
        unique=True,
        nullable=False,
        index=True,
    )

    embedding = Column(
        JSON,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )