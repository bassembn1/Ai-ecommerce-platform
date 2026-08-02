from sqlalchemy.orm import Session

from app.database.models.product_embedding import ProductEmbedding


def get_product_embedding(
    db: Session,
    product_id: int,
):

    return (
        db.query(ProductEmbedding)
        .filter(
            ProductEmbedding.product_id == product_id
        )
        .first()
    )


def save_product_embedding(
    db: Session,
    product_id: int,
    embedding: list[float],
):

    record = get_product_embedding(
        db,
        product_id,
    )

    if record is None:

        record = ProductEmbedding(
            product_id=product_id,
            embedding=embedding,
        )

        db.add(record)

    else:

        record.embedding = embedding

    db.commit()

    db.refresh(record)

    return record