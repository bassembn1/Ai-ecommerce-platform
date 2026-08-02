import json
import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="localhost",
        port=5672,
        credentials=pika.PlainCredentials(
            "admin",
            "admin123"
        )
    )
)


channel = connection.channel()


channel.queue_declare(
    queue="user_events",
    durable=True
)


event = {
    "event_type": "product_created",
    "product_id": 1,
    "event_data": {
        "name": "iPhone 15",
        "category": "phone",
        "brand": "Apple",
        "price": 1200
    }
}


channel.basic_publish(
    exchange="",
    routing_key="user_events",
    body=json.dumps(event)
)


print("Event sent successfully")


connection.close()