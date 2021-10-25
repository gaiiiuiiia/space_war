from app.classes.base.weapon.Weapon import Weapon


class LaserCanon(Weapon):

    def fire(self):
        raise NotImplementedError('That method must be implemented')