from app.database.database import SessionLocal

from app.services.recommendation_service import (
    generate_recommendations,
)


def generate_recommendation_job(user_id: int):

    db = SessionLocal()

    try:
        generate_recommendations(
            db=db,
            user_id=user_id,
        )

    finally:
        db.close()