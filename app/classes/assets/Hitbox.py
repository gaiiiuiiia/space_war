# for referring to current class in typehint
from __future__ import annotations

from app.classes.assets.Coordinate import Coordinate
from app.classes.assets.Size import Size


class Hitbox:

    # TODO must use Rect here

    def __init__(self, coordinate: Coordinate, size: Size):
        self.__coordinate = coordinate
        self.__size = size

    def is_collide(self, hitbox: Hitbox):
        raise NotImplementedError('That method must be implemented')

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
