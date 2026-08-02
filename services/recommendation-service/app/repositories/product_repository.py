from sqlalchemy.orm import Session

from app.database.models.product_snapshot import ProductSnapshot


def get_product(
    db: Session,
    product_id: int,
):

    return (
        db.query(ProductSnapshot)
        .filter(
            ProductSnapshot.product_id == product_id
        )
        .first()
    )


def save_product(
    db: Session,
    product: ProductSnapshot,
):

    db.merge(product)

    db.commit()

    db.refresh(product)

    return product