from typing import NoReturn

import arcade

from game.apple import Apple
from game.snake import Snake


class GameWindow(arcade.Window):

    def __init__(self, width: int, height: int, title: str) -> NoReturn:
        super().__init__(width, height, title)

        self.snake = None

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self) -> NoReturn:
        self.snake: Snake = Snake()
        self.start_key = False
        self.points = 0
        self.apple = Apple(10, 10)

    def on_draw(self) -> NoReturn:
        arcade.start_render()

        # Escribimos la puntuacion
        arcade.draw_text(f"{self.points} points", 10, 20, arcade.color.WHITE, 16)

        self.apple.draw()
        self.snake.draw()

    def update(self, delta_time: float):
        if not self.start_key:
            return

        # Miramos si hemos chocado con la manzana
        hit_list: list = arcade.check_for_collision_with_list(self.apple, self.snake)

        if len(hit_list):
            self.apple = Apple(10, 10)
            self.points += 1
            self.snake.eat_apple()

        self.snake.update()
        self.snake.update_animation()
