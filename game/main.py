from typing import NoReturn

import arcade

from game.factory_game_window import FactoryGameWindow
from game.movement import SCREEN_WIDTH, SCREEN_HEIGHT

SCREEN_TITLE: str = "Snake game by yuan_tr"


def main() -> NoReturn:
    window: arcade.Window = FactoryGameWindow.get_game_window("m", SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    try:
        window.setup()
        arcade.run()
    except:
        window.close()


if __name__ == '__main__':
    main()