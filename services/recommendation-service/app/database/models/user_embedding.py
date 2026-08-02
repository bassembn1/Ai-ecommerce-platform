from sqlalchemy import (
    Column,
    Integer,
    JSON,
)
from app.database.database import Base

class UserEmbedding(Base):

    __tablename__ = "user_embeddings"

    id = Column(
        Integer,
        primary_key=True,
    )

    user_id = Column(
        Integer,
        unique=True,
        nullable=False,
    )

    embedding = Column(
        JSON,
        nullable=False,
    )