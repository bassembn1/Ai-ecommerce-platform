from app.database.database import Base

from app.services.embedding_service import (
    create_product_embedding,
)


def generate_product_embedding_job(
    product_id: int,
):

    db = SessionLocal()

    try:

        create_product_embedding(
            db=db,
            product_id=product_id,
        )

    finally:

        db.close()