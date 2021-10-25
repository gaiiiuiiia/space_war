import pygame as pg
from app.config import config as conf
from app.classes.Player import Player
from app.classes.ObjectManager import ObjectManager


class SpaceWars:
    def __init__(self):
        pg.init()
        pg.display.set_caption(conf.GAME_NAME)
        self.window = pg.display.set_mode(conf.WIN_SIZE)
        self.objectManager = ObjectManager(Player())

    def run(self):
        pass


def main():
    sw = SpaceWars()
    sw.run()


def test():
    pass


if __name__ == '__main__':
    test()
