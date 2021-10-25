from abc import ABC, abstractmethod


class Weapon(ABC):

    def __init__(self, damage: int, energy: int):
        self.__damage = damage
        self.__energy = energy

    @abstractmethod
    def fire(self):
        pass

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value: int):
        self.__damage = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value: int):
        self.__energy = value
