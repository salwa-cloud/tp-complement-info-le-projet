import datetime

from .player import Player


class Game:

    def __init__(
        self,
        player1: Player,
        player2: Player,
        game_mode: str,
        winner: Player,
        #description: str,
        timestamp: datetime,
        ) -> None:

        self.id_game = None
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        self.winner = winner
        self.description = f"Jeu de {self.game_mode} entre {self.player1} et {self.player2}"
        self.timestamp = timestamp

    def __str__(self) -> str:
        if self.winner is None:
            return f"{self.game_mode} between {self.player1} and {self.player2}. Draw"
        return f"{self.game_mode} between {self.player1} and {self.player2}. Winner: {self.winner}"
