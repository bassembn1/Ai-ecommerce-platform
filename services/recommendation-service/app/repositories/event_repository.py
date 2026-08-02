from sqlalchemy.orm import Session

from app.database.models.user_event import UserEvent


def save(
    db: Session,
    event: UserEvent,
):

    db.add(event)

    db.commit()

    db.refresh(event)

    return event