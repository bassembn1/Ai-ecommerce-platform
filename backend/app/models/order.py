from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.database.base import Base
from datetime import datetime, timezone
from enum import Enum as PyEnum
from sqlalchemy import Enum as SQLEnum

class OrderStatus(str, PyEnum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class Order(Base):
    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    total_price = Column(
    Float,
    nullable=False,
)

    status = Column(
        SQLEnum(OrderStatus),
        default=OrderStatus.PENDING,
        nullable=False,
    )

    created_at = Column(
    DateTime(timezone=True),
    default=lambda: datetime.now(timezone.utc),
    nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    items = relationship(
    "OrderItem",
    back_populates="order",
    cascade="all, delete-orphan",
    )





class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(
        Integer,
        primary_key=True
    )

    order_id = Column(
        Integer,
        ForeignKey("orders.id")
    )

    product_id = Column(
    Integer,
    ForeignKey("products.id"),
    )

    quantity = Column(
    Integer,
    nullable=False,
    )

    price = Column(
    Float,
    nullable=False,
)

    order = relationship(
        "Order",
        back_populates="items"
    )

    product = relationship(
    "Product"
)

