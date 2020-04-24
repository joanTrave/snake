from game.game_window import GameWindow
from game.game_window_automatic import GameWindowAutomatic
from game.game_window_manual import GameWindowManual


class FactoryGameWindow:

    @staticmethod
    def get_game_window(game_type: str, width: int, height: int, title: str) -> GameWindow:
        if game_type == "m":
            return GameWindowManual(width, height, title)
        elif game_type == "a":
            return GameWindowAutomatic(width, height, title)