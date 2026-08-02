from sqlalchemy.orm import Session

from app.ai.embedding_service import (
    generate_product_embedding,
)

from app.database.models.product_snapshot import (
    ProductSnapshot,
)

from app.repositories.embedding_repository import (
    save_product_embedding,
)

from app.ai.vector_store import (
    upsert_product_vector,
)


def create_product_embedding(
    db: Session,
    product_id: int,
):

    product = (
        db.query(ProductSnapshot)
        .filter(
            ProductSnapshot.product_id == product_id
        )
        .first()
    )

    if product is None:
        return None

    embedding = generate_product_embedding(
        product
    )
    payload = {
    "name": product.name,
    "category": product.category,
    "brand": product.brand,
    "price": product.price,
    }

    upsert_product_vector(
        product_id=product.product_id,
        embedding=embedding,
        payload=payload,
    )

    return save_product_embedding(
        db=db,
        product_id=product.product_id,
        embedding=embedding,
    )