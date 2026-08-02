""" from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database.models import UserEvent





def get_popular_products(
    db: Session,
    limit: int = 10,
):
    rows = (
        db.query(
            UserEvent.product_id,
            func.count(UserEvent.product_id).label("score"),
        )
        .filter(
            UserEvent.event_type == "view_product"
        )
        .group_by(UserEvent.product_id)
        .order_by(
            func.count(UserEvent.product_id).desc()
        )
        .limit(limit)
        .all()
    )

    return [
        {
            "product_id": row.product_id,
            "score": row.score,
        }
        for row in rows
    ]

def calculate_score(
    category_score: float,
    brand_score: float,
    popularity_score: float,
) -> float:
    return (
        category_score * 0.5
        + brand_score * 0.3
        + popularity_score * 0.2
    ) """

from sqlalchemy.orm import Session

from app.database.models.product_snapshot import ProductSnapshot
from app.database.models.recommendation import Recommendation
from app.repositories.recommendation_repository import (
    delete_user_recommendations,
    save_recommendations,
)
from app.repositories.user_profile_repository import (
    get_user_profile,
)

def calculate_score(
    profile,
    product,
):

    score = 0
    preferences = profile.preferences or {}

    categories = preferences.get("categories", {})

    brands = preferences.get("brands", {})

    score += categories.get(
        product.category,
        0,
    )

    score += brands.get(
        product.brand,
        0,
    )

    return score

def generate_recommendations(
    db: Session,
    user_id: int,
):

    profile = get_user_profile(
        db,
        user_id,
    )

    if profile is None:
        return


    delete_user_recommendations(
        db,
        user_id,
    )


    products = (
        db.query(ProductSnapshot)
        .all()
    )

    recommendations = []


    for product in products:

        score = calculate_score(
            profile,
            product,
        )

        if score == 0:
            continue


        recommendations.append(
            Recommendation(
                user_id=user_id,
                product_id=product.product_id,
                score=score,
            )
        )


    recommendations.sort(
        key=lambda x: x.score,
        reverse=True,
    )


    save_recommendations(
        db,
        recommendations[:20],
    )