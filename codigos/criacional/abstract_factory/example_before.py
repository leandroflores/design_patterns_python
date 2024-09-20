class MySQLConnection:
    def connect(self) -> None:
        print("Connecting MySQL ...")


class MongoDBConnection:
    def connect(self) -> None:
        print("Connecting Mongo DB ...")


class MySQLCommand:
    def execute(query: str) -> None:
        print("MySQL Command: " + query)


class MongoDBCommand:
    def execute(query: str) -> None:
        print("MongoDB Command: " + query)


def app():
    db = "MySQL"

    if db == "MySQL":
        connection = MySQLConnection()
        connection.connect()
        command = MySQLCommand()
        command.execute("SELECT * FROM users;")
    elif db == "MongoDB":
        connection = MongoDBConnection()
        connection.connect()
        command = MongoDBCommand()
        command.execute("{ find: 'users' }")
