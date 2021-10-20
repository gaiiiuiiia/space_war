import pygame as pg
import os
import sys


class SpaceWars:
    def __init__(self):
        print('path is ', os.path.dirname(__file__))

    def run(self):
        pass


def main():
    sw = SpaceWars()
    sw.run()


if __name__ == '__main__':
    main()
