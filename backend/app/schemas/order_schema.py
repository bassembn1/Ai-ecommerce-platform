from pydantic import BaseModel


class OrderItemRequest(
    BaseModel
):
    product_id: int
    quantity: int
    price: float


class OrderRequest(
    BaseModel
):
    items: list[
        OrderItemRequest
    ]

    total_price: float