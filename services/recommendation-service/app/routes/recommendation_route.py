""" 

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.services.recommendation_service import (
    get_popular_products,
)

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/popular")
def popular_products(
    limit: int = 10,
    db: Session = Depends(get_db),
):
    return get_popular_products(
        db=db,
        limit=limit,
    ) """

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal

# from app.dependencies.auth import get_current_user

from app.repositories.recommendation_repository import (
    get_user_recommendations,
)

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"],
)


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/{user_id}")
def get_recommendations(
    user_id: int,
    db: Session = Depends(get_db),
):
    return get_user_recommendations(
        db=db,
        user_id=user_id,
    )