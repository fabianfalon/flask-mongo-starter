import pika
import os


class RabbitPublisher:
    def __init__(self, config):
        self.config = config

    def publish(self, routing_key, message):
        connection = self.create_connection()

        channel = connection.channel()
        channel.exchange_declare(
            exchange=self.config["exchange"], exchange_type="topic"
        )
        # Publishes message to the exchange with the given routing key
        channel.basic_publish(
            exchange=self.config["exchange"], routing_key=routing_key, body=message
        )

    def create_connection(self):

        user = os.getenv("RABBITMQ_USER", "guest")
        password = os.getenv("RABBITMQ_PASS", "guest")

        credentials = pika.PlainCredentials(user, password)

        param = pika.ConnectionParameters(
            host=self.config["host"], port=self.config["port"], credentials=credentials
        )

        return pika.BlockingConnection(param)
