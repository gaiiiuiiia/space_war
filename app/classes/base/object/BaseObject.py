from abc import ABC, abstractmethod
from app.classes.assets.Coordinate import Coordinate
from app.classes.assets.Size import Size


class BaseObject(ABC):

    def __init__(self, coordinate: Coordinate, size: Size, speed: float):
        self.__coordinate = coordinate
        self.__size = size
        self.__speed = speed

    @abstractmethod
    def draw(self):
        pass

    @property
    def coordinate(self):
        return self.__coordinate

    @coordinate.setter
    def coordinate(self, value: Coordinate):
        self.__coordinate = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value: Size):
        self.__size = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value: float):
        self.__speed = value
