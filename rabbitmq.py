import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


class Rabbit:
    def __init__(self, host):
        self.host = host

    def get_rabbit(self):
        # todo
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.host))
        return connection
