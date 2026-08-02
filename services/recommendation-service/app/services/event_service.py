from app.repositories.event_repository import save

from app.database.models.user_event import UserEvent


def save_event(
    db,
    event_data,
):

    event = UserEvent(
        user_id=event_data["user_id"],
        event_type=event_data["event_type"],
        product_id=event_data["product_id"],
        event_data=event_data.get("event_data"),
    )

    return save(
        db,
        event,
    )