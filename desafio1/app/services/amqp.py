import os
import pika

AMQP_URL = os.getenv("AMQP_URL", "amqp://guest:guest@rabbitmq:5672/")

def publish_message(message):
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()
    channel.queue_declare(queue="sua_fila")
    channel.basic_publish(exchange="", routing_key="sua_fila", body=str(message))
    connection.close()