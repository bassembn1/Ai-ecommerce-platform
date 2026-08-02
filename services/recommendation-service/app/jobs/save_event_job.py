from app.database.database import SessionLocal
from app.services.event_service import save_event


def save_event_job(event: dict):

    db = SessionLocal()

    try:

        save_event(
            db=db,
            event_data=event,
        )

    finally:

        db.close()