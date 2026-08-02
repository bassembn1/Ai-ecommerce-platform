from fastapi import (
    APIRouter
)

from pydantic import (
    BaseModel
)

from app.services.stripe_service import (
    create_checkout_session
)

router = APIRouter()


class CheckoutRequest(
    BaseModel
):
    items: list


@router.post(
    "/create-checkout-session"
)
def checkout(
    request:
    CheckoutRequest
):
    url = create_checkout_session(request.items)

    return {
        "url": url
    }