from enum import Enum

class EventType(str, Enum):
    PRODUCT_CREATED = "product_created"
    PRODUCT_UPDATED = "product_updated"
    VIEW_PRODUCT = "view_product"
    ADD_TO_CART = "add_to_cart"
    PURCHASE = "purchase"