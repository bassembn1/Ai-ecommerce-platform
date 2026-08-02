""" import json

from app.database import SessionLocal
from app.models import UserEvent



def process_event(body: bytes):

    event = json.loads(body)


    db = SessionLocal()

    try:

        user_event = UserEvent(
            user_id=event["user_id"],
            event_type=event["event_type"],
            product_id=event.get("product_id"),
            event_data=event.get("event_data"),
        )


        db.add(user_event)

        db.commit()


        print(
            "Event saved:",
            event
        )
     except Exception as e:
        db.rollback()
        print(f"Error: {e}")


    finally:

        db.close() """

""" import json

from app.database.database import SessionLocal
from app.services.event_service import save_event


def process_event(body: bytes):

    event = json.loads(body)

    db = SessionLocal()

    try:

        save_event(
            db=db,
            event=event,
        )

        print(
            "Event saved successfully."
        )

    finally:
        db.close() """

""" import json

from app.dispatcher import dispatch_event


def process_event(body: bytes):

    event = json.loads(body)

    dispatch_event(event)

connection, channel = create_connection()

channel.basic_consume(
    queue="user_events",
    on_message_callback=callback,
)

channel.start_consuming() """

import json

from app.dispatcher import dispatch_event
from app.services.rabbitmq import create_connection


def callback(ch, method, properties, body):

    event = json.loads(body)
    print("📩 Event received:", flush=True)
    print(event, flush=True)

    dispatch_event(event)

    ch.basic_ack(
        delivery_tag=method.delivery_tag,
    )


connection, channel = create_connection()

channel.basic_qos(prefetch_count=1)

channel.basic_consume(
    queue="user_events",
    on_message_callback=callback,
)

print("Worker started...", flush=True)

channel.start_consuming()