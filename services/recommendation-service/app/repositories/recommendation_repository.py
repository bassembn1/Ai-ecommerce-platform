from sqlalchemy.orm import Session

from app.database.models.recommendation import Recommendation


def delete_user_recommendations(
    db: Session,
    user_id: int,
):

    (
        db.query(Recommendation)
        .filter(
            Recommendation.user_id == user_id
        )
        .delete()
    )

    db.commit()


def save_recommendations(
    db: Session,
    recommendations: list[Recommendation],
):

    db.add_all(recommendations)

    db.commit()

def get_user_recommendations(
    db: Session,
    user_id: int,
):

    return (
        db.query(Recommendation)
        .filter(
            Recommendation.user_id == user_id
        )
        .order_by(
            Recommendation.score.desc()
        )
        .limit(20)
        .all()
    )