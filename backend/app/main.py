from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.logging import logger

from app.database.base import Base
from app.database.db import engine

# Import models so SQLAlchemy registers them
from app.models.order import Order, OrderItem
from app.models.product import Product
from app.models.user import User

from app.api.router import register_routes


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
)


logger.info("Backend Started Successfully")


Base.metadata.create_all(
    bind=engine
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register all API routes
register_routes(app)


@app.get("/")
def home():
    return {
        "message": "Amazon AI Commerce API",
        "status": "running",
        "version": "1.0.0",
    }