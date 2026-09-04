from .gamemode import GameMode
from .coinflipmode import CoinFlipMode
from .dicemode import DiceMode

class GameModeFactory:
    @classmethod
    def get_mode(cls, game_mode: str) -> GameMode:
        """
        Returns the corresponding GameMode object.
        Args:
            game_mode (str): The identifier of the game mode (e.g., 'coinflip', 'dice').
        Returns:
            GameMode: An instance of a class implementing GameMode.
        Raises:
            ValueError: If the requested game_mode is not supported.
        """

        if game_mode == 'coinflip':
            return CoinFlipMode()
        elif game_mode == 'dice':
            return DiceMode()
        else:
            raise ValueError("le game_mode entré n'est pas reconnu dans notre application")
