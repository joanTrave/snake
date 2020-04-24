from typing import NoReturn

import arcade

from game.factory_game_window import FactoryGameWindow
from game.game_window import GameWindow

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Snake game by yuan_tr"


def main() -> NoReturn:
    window: arcade.Window = FactoryGameWindow.get_game_window("m", SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()