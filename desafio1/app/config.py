import os

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")

AMQP_URL = os.getenv("AMQP_URL", "amqp://guest:guest@rabbitmq:5672/")
AMQP_QUEUE = os.getenv("AMQP_QUEUE", "publications")
