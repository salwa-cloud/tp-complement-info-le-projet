from .gamemode import Game_Mode
from .game import Game
from datetime import date

class DiceMode(Game_Mode):
    def play(self, p1, p2) -> Game:
        d1 = secrets.choice(range(1, 7))
        d2 = secrets.choice(range(1, 7))
        if d1 > d2:
            winner = p1
        elif d1 < d2:
            winner = p2
        else:
            inner = None


        return Game(
                    payer1= p1,
                    player2=p2,
                    game_mode: f" jeux de dice ",
                    winner: winner,
                    timestamp: date.today())

