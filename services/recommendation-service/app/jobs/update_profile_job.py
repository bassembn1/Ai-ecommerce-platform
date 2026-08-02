from app.database.database import SessionLocal

from app.services.profile_service import (
    update_user_profile,
)


def update_profile_job(
    user_id: int,
):

    db = SessionLocal()

    try:

        update_user_profile(
            db,
            user_id,
        )

    finally:

        db.close()