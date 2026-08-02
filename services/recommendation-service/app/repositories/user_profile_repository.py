from sqlalchemy.orm import Session

from app.database.models.user_profile import UserProfile


def get_user_profile(
    db: Session,
    user_id: int,
):

    return (
        db.query(UserProfile)
        .filter(
            UserProfile.user_id == user_id
        )
        .first()
    )


def save_user_profile(
    db: Session,
    profile: UserProfile,
):

    db.merge(profile)

    db.commit()

    db.refresh(profile)

    return profile