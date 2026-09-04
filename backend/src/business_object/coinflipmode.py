from .gamemode import GameMode
from .game import GAme

class CoinFlipMode(GameMode):
     def play(self, player_id, opponent_id, game_mode, choice="heads"):
        if game_mode == "coinflip":
            result = secrets.choice(["heads", "tails"])
            winner = p1 if result == choice else p2
        elif game_mode == "dice":
            d1 = secrets.choice(range(1, 7))
            d2 = secrets.choice(range(1, 7))
            if d1 > d2:
              winner = p1
            elif d1 < d2:
              winner = p2
            else:
              winner = None              