from typing import NoReturn

import arcade

from game.snake import Snake


class GameWindow(arcade.Window):

    def __init__(self, width: int, height: int, title: str) -> NoReturn:
        super().__init__(width, height, title)

        self.start_key = False

        self.snake = None

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self) -> NoReturn:
        self.snake: Snake = Snake()

    def on_draw(self) -> NoReturn:
        arcade.start_render()
        self.snake.draw()
