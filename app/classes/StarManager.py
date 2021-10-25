from app.interfaces.Observable import Observable
from app.interfaces.Observer import Observer
import app.config.config as conf
from app.classes.Star import Star
from app.classes.assets.Coordinate import Coordinate
from app.classes.assets.Size import Size
import random as rnd


class StarManager(Observer):

    def __init__(self):
        self.__stars = {}
        self.__initialize_stars()

    def __initialize_stars(self):
        for i in range(conf.ENVIRONMENT_PARTICLE_AMOUNT):
            self.__add_new_star()

    def __add_new_star(self):
        coordinate = Coordinate.generate_coordinate_out_of_screen(10)
        side_size = rnd.randint(conf.ENVIRONMENT_PARTICLE_MIN_SIZE, conf.ENVIRONMENT_PARTICLE_MAX_SIZE)
        star = Star(coordinate=coordinate,
                    size=Size(side_size, side_size),
                    speed=side_size)

        self.__stars[hash(star)] = star

    def update(self, observable: Observable):
        self.__stars.pop(hash(observable))
        self.__add_new_star()
