import pika
import json
import logging
import os


logging.basicConfig(level="INFO")


class RabbitSubscriber:
    def __init__(self, queueName, bindingKey, config):
        self.queueName = queueName
        self.bindingKey = bindingKey
        self.config = config
        self.connection = self._create_connection()

    def __del__(self):
        self.connection.close()

    def _create_connection(self):

        user = os.getenv("RABBITMQ_USER", "rootuser")
        password = os.getenv("RABBITMQ_PASS", "mypassverystrong")
        credentials = pika.PlainCredentials(user, password)
        parameters = pika.ConnectionParameters(
            host=self.config["host"], port=self.config["port"], credentials=credentials
        )
        return pika.BlockingConnection(parameters)

    def on_message_callback(self, channel, method, properties, body):
        binding_key = method.routing_key
        logging.info(f"received new message for {binding_key}")
        if body:
            data = json.loads(body)
            logging.info(f"data processed ok: {data}")

    def setup(self):
        channel = self.connection.channel()
        channel.exchange_declare(
            exchange=self.config["exchange"], exchange_type="topic"
        )
        # This method creates or checks a queue
        channel.queue_declare(queue=self.queueName)

        # Binds the queue to the specified exchang
        channel.queue_bind(
            queue=self.queueName,
            exchange=self.config["exchange"],
            routing_key=self.bindingKey,
        )

        channel.basic_consume(
            queue=self.queueName,
            on_message_callback=self.on_message_callback,
            auto_ack=True,
        )
        logging.info(f"[*] Waiting for data for . To exit press CTRL+C")
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
