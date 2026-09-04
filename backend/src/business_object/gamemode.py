from abc import ABC, abstractmethod

from .game import Game
from .player import Player


class GameMode(ABC):
    @abstractmethod 
    def play(self, p1: Player, p2: Player) -> Game:
        """Joue une partie entre p1 et p2 et retourne un objet Game"""
        pass