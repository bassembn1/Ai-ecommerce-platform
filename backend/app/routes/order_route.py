from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
)

from sqlalchemy.orm import Session

from app.database.db import (
    SessionLocal,
)

from app.models.order import (
    Order,
    OrderItem,
)

from app.schemas.order_schema import (
    OrderRequest,
)

from app.core.security import (
    verify_token,
)

router = APIRouter()

security = HTTPBearer()


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/orders")
def create_order(
    order: OrderRequest,

    credentials:
    HTTPAuthorizationCredentials =
    Depends(security),

    db: Session =
    Depends(get_db),
):
    token = (
        credentials.credentials
    )

    payload = (
        verify_token(token)
    )

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )

    user_id = payload[
        "user_id"
    ]

    new_order = Order(
        user_id=user_id,
        total_price=
        order.total_price,
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for item in order.items:
        db.add(
            OrderItem(
                order_id=
                new_order.id,
                product_id=
                item.product_id,
                quantity=
                item.quantity,
                price=
                item.price,
            )
        )

    db.commit()

    return {
        "message":
        "Order created"
    }


@router.get("/my-orders")
def get_my_orders(
    credentials:
    HTTPAuthorizationCredentials =
    Depends(security),

    db: Session =
    Depends(get_db),
):
    token = (
        credentials.credentials
    )

    payload = (
        verify_token(token)
    )

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )

    user_id = payload[
        "user_id"
    ]

    orders = (
        db.query(Order)
        .filter(
            Order.user_id ==
            user_id
        )
        .all()
    )

    return orders