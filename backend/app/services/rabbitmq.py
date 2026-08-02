import json
import pika

from app.core.config import settings


QUEUE_NAME = "user_events"


def publish_event(event: dict):

    print(
        "DEBUG RABBIT:",
        settings.RABBITMQ_HOST,
        settings.RABBITMQ_PORT,
        settings.RABBITMQ_USER,
        settings.RABBITMQ_PASSWORD
    )

    credentials = pika.PlainCredentials(
        username=settings.RABBITMQ_USER,
        password=settings.RABBITMQ_PASSWORD,
    )

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            credentials=credentials,
        )
    )

    channel = connection.channel()

    channel.queue_declare(
        queue=QUEUE_NAME,
        durable=True,
    )

    channel.basic_publish(
        exchange="",
        routing_key=QUEUE_NAME,
        body=json.dumps(event),
        properties=pika.BasicProperties(
            delivery_mode=2
        ),
    )

    print("EVENT SENT:", event)

    connection.close()