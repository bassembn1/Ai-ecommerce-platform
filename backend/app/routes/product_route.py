from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.models.product import Product
from app.schemas.product_schema import ProductResponse
from app.schemas.product_schema import (
    ProductCreate
)

from app.services.auth_guard import get_current_admin


from app.models.user import (
    User
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/products", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.get(
    "/products/{product_id}",
    response_model=ProductResponse
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        return {"error": "Product not found"}

    return product

@router.post("/products")
def create_product(
    product:
    ProductCreate,

    authorization:
    str = Header(None),

    db: Session =
    Depends(get_db),
):

    new_product =Product(
        title=
        product.title,

        description=
        product.description,

        price=
        product.price,

        image=
        product.image,
    )

    db.add(
        new_product
    )

    db.commit()

    return {
        "message":
        "Product added"
    }

@router.get("/admin/products")
def get_all_products(
    authorization: str = Header(None),
    db: Session = Depends(get_db),
):
    from app.services.auth_guard import get_current_admin

    get_current_admin(authorization, db)

    return db.query(Product).all()

@router.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    authorization: str = Header(None),
    db: Session = Depends(get_db),
):
    from app.services.auth_guard import get_current_admin

    get_current_admin(authorization, db)

    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        return {"error": "Product not found"}

    db.delete(product)
    db.commit()

    return {"message": "Deleted"}