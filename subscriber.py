from src.config import BaseConfig

from src.bus.rabbit.subscriber import RabbitSubscriber
config = BaseConfig()


class Subscriber(RabbitSubscriber):
    pass


if __name__ == '__main__':

    config = {
        "host": config.RABBIT_HOSTNAME,
        "port": config.RABBIT_PORT,
        "exchange": config.RABBIT_EXCHANGE
    }
    subs = Subscriber("my_exchange", "update_message_topic", config)
    subs.setup()
