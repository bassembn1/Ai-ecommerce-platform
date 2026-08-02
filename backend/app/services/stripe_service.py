import stripe
import os
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv(
    "STRIPE_SECRET_KEY"
)


def create_checkout_session(
    items
):
    line_items = []

    for item in items:
        line_items.append(
            {
                "price_data": {
                    "currency":
                    "usd",

                    "product_data": {
                        "name":
                        item["title"]
                    },

                    "unit_amount":
                    int(
                        item["price"]
                        * 100
                    ),
                },

                "quantity":
                1,
            }
        )

    session = (
        stripe.checkout.Session.create(
            payment_method_types=[
                "card"
            ],

            line_items=line_items,

            mode="payment",

            success_url=
            f"{os.getenv('FRONTEND_URL')}/success",

            cancel_url=
            f"{os.getenv('FRONTEND_URL')}/cart",
        )
    )

    return session.url