from contextlib import asynccontextmanager
from threading import Thread

from fastapi import FastAPI

from app.consumer import start_consumer
from app.core.logging import logger

from app.database.database import Base, engine
from app.database.models import UserEvent, ProductSnapshot


consumer_thread = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global consumer_thread

    logger.info(
        "Starting Recommendation Service..."
    )

    Base.metadata.create_all(bind=engine)

    consumer_thread = Thread(
        target=start_consumer,
        daemon=True,
    )

    consumer_thread.start()

    yield

    logger.info(
        "Stopping Recommendation Service..."
    )