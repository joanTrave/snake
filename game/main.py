from typing import NoReturn

import arcade

from game.game_window import GameWindow

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Snake game by yuan_tr"


def main() -> NoReturn:
    window: arcade.Window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()