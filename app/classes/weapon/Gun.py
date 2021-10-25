from app.classes.base.weapon.Weapon import Weapon


class Gun(Weapon):

    def fire(self):
        raise NotImplementedError('That method must be implemented')
