from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    image = Column(String)
    category = Column(String)
    brand = Column(String)
    sku = Column(String)
    stock = Column(Integer)
    is_active = Column(Boolean, default=True)