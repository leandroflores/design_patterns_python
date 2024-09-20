from abc import ABC, abstractmethod


class Connection(ABC):
    @abstractmethod
    def connect(self) -> None: ...


class Command(ABC):
    @abstractmethod
    def execute(self, query: str) -> None: ...


class DBFactory(ABC):
    @abstractmethod
    def create_connection(self) -> Connection: ...

    @abstractmethod
    def create_command(self) -> Command: ...


class MySQLConnection(Connection):
    def connect(self) -> None:
        print("Connecting MySQL ...")


class MySQLCommand:
    def execute(query: str) -> None:
        print("MySQL Command: " + query)


class MongoDBConnection(Connection):
    def connect(self) -> None:
        print("Connecting MongoDB ...")


class MongoDBCommand:
    def execute(query: str) -> None:
        print("MongoDB Command: " + query)


class MySQLFactory(DBFactory):
    def create_connection(self) -> Connection:
        return MySQLConnection()

    def create_command(self) -> Command:
        return MySQLCommand()


class MongoDBFactory(DBFactory):
    def create_connection(self) -> Connection:
        return MongoDBConnection()

    def create_command(self) -> Command:
        return MongoDBCommand()


def app():
    db = "MongoDB"

    if db == "MySQL":
        factory = MySQLFactory()
    elif db == "MongoDB":
        factory = MongoDBFactory()

    connection = factory.create_connection()
    connection.connect()

    command = factory.create_command()
    command.execute("{ find: 'users' }")
