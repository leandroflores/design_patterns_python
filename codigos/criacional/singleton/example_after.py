class SessionSingleton:
    _instance: "SessionSingleton" = None

    def __init__(self) -> None:
        self.host: str = "localhost"
        self.user: str = "root"
        self.port: str = "5403"

    @classmethod
    def instance(cls) -> "SessionSingleton":
        if not cls._instance:
            cls._instance = cls()
        return cls._instance


session_1: SessionSingleton = SessionSingleton.instance()
session_2: SessionSingleton = SessionSingleton.instance()

print(id(session_1))
print(id(session_2))
print(id(session_1) == id(session_2))
