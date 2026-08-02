import json

from app.services.rabbitmq import create_connection
from app.worker import process_event


def callback(ch, method, properties, body):

    process_event(body)

    ch.basic_ack(
        delivery_tag=method.delivery_tag,
    )


def start_consumer():

    connection, channel = create_connection()




    channel.basic_consume(
        queue="user_events",
        on_message_callback=callback,
        auto_ack=False
    )

    print("Recommendation service waiting for events...")

    channel.start_consuming()