from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MySQL database")


class MongoDB(Database):
    def save(self, data):
        print(f"Saving {data} to MongoDB")


class DataManager:
    def __init__(self, database: Database):
        self.database = database

    def save_data(self, data):
        self.database.save(data)

mysql_db = MySQLDatabase()
mongo_db = MongoDB()

data_manager1 = DataManager(mysql_db)
data_manager2 = DataManager(mongo_db)

data_manager1.save_data("User Info")
data_manager2.save_data("User Info")
