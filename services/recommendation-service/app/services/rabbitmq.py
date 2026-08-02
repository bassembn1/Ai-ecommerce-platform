""" import pika

from app.core.config import settings

QUEUE_NAME = "user_events"


def create_connection():
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

    return connection, channel """

import time
import pika

from app.core.config import settings

QUEUE_NAME = "user_events"


def create_connection():
    credentials = pika.PlainCredentials(
        settings.RABBITMQ_USER,
        settings.RABBITMQ_PASSWORD,
    )

    while True:
        try:
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

            print("✅ Connected to RabbitMQ")

            return connection, channel

        except pika.exceptions.AMQPConnectionError:
            print("⏳ RabbitMQ is not ready. Retrying in 5 seconds...")
            time.sleep(5)