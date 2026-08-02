from sqlalchemy.orm import Session

from app.database.models.user_profile import UserProfile
from app.database.models.user_event import UserEvent
from app.database.models.product_snapshot import ProductSnapshot

from app.repositories.user_profile_repository import (
    get_user_profile,
    save_user_profile,
)


EVENT_WEIGHTS = {
    "view_product": 1,
    "add_to_cart": 3,
    "purchase": 5,
}


def update_user_profile(
    db: Session,
    user_id: int,
):

    events = (
        db.query(
            UserEvent
        )
        .filter(
            UserEvent.user_id == user_id
        )
        .all()
    )


    categories = {}
    brands = {}


    for event in events:

        if not event.product_id:
            continue


        product = (
            db.query(ProductSnapshot)
            .filter(
                ProductSnapshot.product_id
                == event.product_id
            )
            .first()
        )


        if not product:
            continue


        weight = EVENT_WEIGHTS.get(
            event.event_type,
            1
        )


        if product.category:

            categories[product.category] = (
                categories.get(
                    product.category,
                    0
                )
                + weight
            )


        if product.brand:

            brands[product.brand] = (
                brands.get(
                    product.brand,
                    0
                )
                + weight
            )


    profile = get_user_profile(
        db,
        user_id,
    )


    if not profile:

        profile = UserProfile(
            user_id=user_id,
        )

        db.add(profile)


    profile.preferences = {
        "categories": categories,
        "brands": brands,
    }


    db.commit()

    db.refresh(profile)


    return save_user_profile(
    db,
    profile,
)