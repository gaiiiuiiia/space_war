from __future__ import annotations
from math import sqrt
import random as rnd
import app.config.config as conf


class Coordinate:

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def distance(self, coordinate: Coordinate) -> float:
        return sqrt((self.x - coordinate.x)**2 - (self.y - coordinate.y)**2)

    @classmethod
    def generate_coordinate_out_of_screen(cls, distance: int) -> Coordinate:

        # horizontal
        if rnd.randint(0, 1) == 0:
            return Coordinate(
                rnd.randint(0 - distance, conf.WIN_WIDTH + distance),
                rnd.choice([0 - distance, conf.WIN_HEIGHT + distance])
            )

        return Coordinate(
            rnd.choice([0 - distance, conf.WIN_WIDTH + distance]),
            rnd.randint(0 - distance, conf.WIN_HEIGHT + distance)
        )

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y
