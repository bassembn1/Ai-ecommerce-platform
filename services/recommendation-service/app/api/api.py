from fastapi import FastAPI
from app.database import SessionLocal
from app.services.recommendation_service import (
    get_most_viewed_products,
)

app = FastAPI()


@app.get("/recommendations/popular")
def popular():

    db = SessionLocal()

    try:

        return get_most_viewed_products(db)

    finally:

        db.close()