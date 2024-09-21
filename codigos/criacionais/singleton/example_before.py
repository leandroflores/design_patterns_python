class Session:
    def __init__(self) -> None:
        self.host: str = "localhost"
        self.user: str = "root"
        self.port: str = "5403"


session_1: Session = Session()
session_2: Session = Session()

print(id(session_1))
print(id(session_2))
print(id(session_1) == id(session_2))
