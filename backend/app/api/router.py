from fastapi import FastAPI

from app.routes.auth_route import router as auth_router
from app.routes.user_route import router as user_router
from app.routes.product_route import router as product_router
from app.routes.order_route import router as order_router
from app.routes.payment_route import router as payment_router
from app.routes.event_route import router as event_router


def register_routes(app: FastAPI):

    app.include_router(auth_router)
    app.include_router(user_router)
    app.include_router(product_router)
    app.include_router(order_router)
    app.include_router(payment_router)
    app.include_router(event_router)