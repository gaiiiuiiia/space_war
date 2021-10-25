from abc import abstractmethod
from app.classes.assets.Size import Size
from app.classes.base.object.BaseObject import BaseObject
from app.classes.assets.Coordinate import Coordinate
from app.classes.assets.Hitbox import Hitbox


class Bullet(BaseObject):
    def __init__(self,
                 coordinate: Coordinate,
                 size: Size,
                 speed: int,
                 damage: int):
        super(Bullet, self).__init__(coordinate, size, speed)
        self.__damage = damage
        self.__hitbox = Hitbox(coordinate, size)

    @abstractmethod
    def do_damage(self):
        pass

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value: int):
        self.__damage = value

    @property
    def hitbox(self):
        return self.__hitbox

    @hitbox.setter
    def hitbox(self, value: Hitbox):
        self.__hitbox = value

    @property
    def coordinate(self):
        return self.__coordinate

    @coordinate.setter
    def coordinate(self, value: Coordinate):
        self.__coordinate = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value: int):
        self.__speed = value
