from app.classes.base.object.BaseObject import BaseObject
from app.classes.assets.Coordinate import Coordinate
from app.classes.base.weapon.Weapon import Weapon
from app.classes.assets.Size import Size


class Unit(BaseObject):
    def __init__(self,
                 coordinate: Coordinate,
                 size: Size,
                 speed: float,
                 hp: int,
                 armor: int,
                 weapon: Weapon):

        super(Unit, self).__init__(coordinate, size, speed)
        self.__hp = hp
        self.__armor = armor
        self.__weapon = weapon

    def draw(self):
        pass

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value: int):
        self.__hp = value

    @property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, value: int):
        self.__armor = value

    @property
    def weapon(self):
        return self.weapon

    @weapon.setter
    def weapon(self, value: Weapon):
        self.__weapon = value
