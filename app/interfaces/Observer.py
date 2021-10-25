from abc import ABC, abstractmethod
from app.interfaces.Observable import Observable


class Observer(ABC):

    @abstractmethod
    def update(self, observable: Observable):
        pass
