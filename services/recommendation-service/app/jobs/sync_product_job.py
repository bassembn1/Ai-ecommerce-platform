from app.database.database import SessionLocal

from app.services.product_service import (
    create_or_update_product,
)


def sync_product_job(
    event: dict,
):

    db = SessionLocal()

    try:

        create_or_update_product(
            db=db,
            event=event,
        )

    finally:

        db.close()