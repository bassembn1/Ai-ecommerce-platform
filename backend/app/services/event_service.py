from app.models.event import Event


def save_event(
    db,
    user_id,
    event_type,
    product_id=None,
    event_data=None,
):
    event = Event(
        user_id=user_id,
        event_type=event_type,
        product_id=product_id,
        event_data=event_data,
    )

    db.add(event)
    db.commit()

    return event