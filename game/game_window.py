from typing import NoReturn

import arcade


class GameWindow(arcade.Window):

    def __init__(self, width: int, height: int, title: str) -> NoReturn:
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self) -> NoReturn:
        pass

    def on_draw(self) -> NoReturn:
        arcade.start_render()

    def on_update(self, delta_time: float) -> NoReturn:
        pass
