import random as rd

import arcade

from game.movement import SCREEN_WIDTH, SCREEN_HEIGHT, COMPONENT_SIZE


class Apple(arcade.SpriteSolidColor):

    def __init__(self, width: int, height: int):
        super().__init__(width, height, arcade.color.RED_DEVIL)
        self.center_x = rd.choice(range(COMPONENT_SIZE//2, SCREEN_WIDTH - 6, COMPONENT_SIZE//2))
        self.center_y = rd.choice(range(COMPONENT_SIZE//2, SCREEN_HEIGHT - 6, COMPONENT_SIZE//2))