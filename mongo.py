from pymongo import MongoClient


class Mongo:
    def __init__(self, host, port, db_name=None, collection_name=None):
        """

        :param host:
        :param port:
        :param db_name:
        :param collection_name:
        """
        self.host = host
        self.port = port
        self.db = db_name
        self.collection_name = collection_name

    def get_collection_object(self):
        client = MongoClient(self.host, self.port)
        db = client[self.db]
        collection = db[self.collection_name]
        return collection

    def get_connection(self):
        return MongoClient(self.host, self.port)


if __name__ == '__main__':
    m = Mongo('192.168.0.235', 27017, 'baiduqianxi', 'baiduqianxi')
    coll = m.get_collection_object()
    for i in coll.find():
        print(i)
        break