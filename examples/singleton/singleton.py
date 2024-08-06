
from typing import Any


class SingletonMeta(type):

    _instances: dict = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):
    
    def some_business_logic(self):
        print("Running logic...")


if __name__ == "__main__":

    s1: Singleton = Singleton()
    s2: Singleton = Singleton()
    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")