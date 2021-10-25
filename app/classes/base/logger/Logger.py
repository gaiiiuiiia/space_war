from abc import abstractmethod
from app.classes.base.Singleton import Singleton


class Logger(Singleton):

    @abstractmethod
    def log(self, message: str):
        pass
