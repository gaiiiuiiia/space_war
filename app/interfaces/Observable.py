from abc import ABC, abstractmethod
from app.interfaces.Observer import Observer


class Observable(ABC):

    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass
