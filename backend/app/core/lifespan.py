from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logging import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Amazon AI Commerce Backend...")

    yield

    logger.info("Stopping Amazon AI Commerce Backend...")