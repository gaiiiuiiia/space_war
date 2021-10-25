from abc import ABC, abstractmethod


class Singleton(ABC):
    __instances = {}

    def __new__(cls, *args, **kwargs):
        if cls.__name__ not in Singleton.__instances.keys():
            Singleton.__instances[cls.__name__] = super(Singleton, cls).__new__(cls)
            Singleton.__instances[cls.__name__].init()
        return Singleton.__instances[cls.__name__]

    @abstractmethod
    def init(self, *args, **kwargs):
        pass

    @classmethod
    def get_instance(cls):
        return cls()
