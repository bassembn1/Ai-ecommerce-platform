from sqlalchemy.orm import Session

from app.database.models.product_snapshot import ProductSnapshot


def create_or_update_product(
    db: Session,
    event: dict,
):

    data = event["event_data"]

    product = (
        db.query(ProductSnapshot)
        .filter(
            ProductSnapshot.product_id == event["product_id"]
        )
        .first()
    )

    if product is None:

        product = ProductSnapshot(
            product_id=event["product_id"],
        )

        db.add(product)

    product.name = data["name"]
    product.category = data["category"]
    product.brand = data["brand"]
    product.price = data["price"]

    db.commit()

    db.refresh(product)

    return product