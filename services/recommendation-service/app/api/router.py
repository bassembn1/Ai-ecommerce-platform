from fastapi import FastAPI

from app.routes.recommendation_route import (
    router as recommendation_router,
)


def register_routes(app: FastAPI):
    app.include_router(
        recommendation_router
    )