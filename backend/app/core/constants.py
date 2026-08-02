from enum import Enum


class UserRole(str, Enum):
    ADMIN = "admin"
    SELLER = "seller"
    CUSTOMER = "customer"


class EventType(str, Enum):
    VIEW_PRODUCT = "view_product"
    ADD_TO_CART = "add_to_cart"
    REMOVE_FROM_CART = "remove_from_cart"
    PURCHASE = "purchase"
    SEARCH = "search"
    LOGIN = "login"
    LOGOUT = "logout"
    WISHLIST_ADD = "wishlist_add"
    REVIEW_CREATE = "review_create"


class OrderStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class PaymentStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    REFUNDED = "refunded"


class PaymentMethod(str, Enum):
    STRIPE = "stripe"
    PAYPAL = "paypal"
    FLOUCI = "flouci"
    CASH_ON_DELIVERY = "cash_on_delivery"