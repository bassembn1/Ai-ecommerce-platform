from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
)

from app.database.database import Base


class ProductSnapshot(Base):

    __tablename__ = "product_snapshots"

    product_id = Column(
        Integer,
        primary_key=True,
    )

    name = Column(String(255))

    description = Column(String)

    category = Column(String(100))

    brand = Column(String(100))

    price = Column(Float)