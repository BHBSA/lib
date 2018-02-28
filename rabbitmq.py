import pika


class Rabbit:
    def __init__(self, host, port):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host, port))

    def get_connection(self):
        return self.connection

    def get_channel(self):
        return self.connection.channel()


if __name__ == '__main__':
    r = Rabbit('192.168.0.190', 5673)
    channel = r.get_channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
    print(" [x] Sent 'Hello World!'")
