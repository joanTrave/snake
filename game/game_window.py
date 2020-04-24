import time
from typing import NoReturn

import random as rd
import arcade

from game.movement import get_new_mov
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

    def on_update(self, delta_time: float) -> NoReturn:
        if not self.start_key:
            return

        time.sleep(0.25)
        if rd.choice(6*[False] + 4*[True]):
            self.snake.direction = get_new_mov(self.snake.direction)
        try:
            self.snake.update()
            self.snake.update_animation()
        except:
            self.start_key = False

    def on_key_press(self, symbol: int, modifiers: int):
        self.start_key = True

        #self.snake.direction =
