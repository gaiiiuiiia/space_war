from app.classes.Player import Player
from app.classes.StarManager import StarManager


class ObjectManager:

    def __init__(self, player: Player):
        self.player = player
        self.starManager = StarManager()
