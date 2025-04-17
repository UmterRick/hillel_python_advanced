"""
D - dependency inversion
"""
from abc import ABC, abstractmethod


class DbDriver(ABC):

    @abstractmethod
    def connect(self):
        raise NotImplementedError
    @abstractmethod
    def save_data(self):
        ...

class MySQLDb(DbDriver):
    def connect(self):
        print("Connected")

    def save_data(self):
        ...

class PostgreSQL(DbDriver):
    def save_data(self):
        ...

class Server:
    def __init__(self, ):
        self.db = PostgreSQL()


class NewServer:
    def __init__(self, db: DbDriver):
        self.db = db


    def start(self):
        self.db.connect()

    def insert(self):
        self.db.insert_data()

server_1 = Server()
del server_1