from typing import NoReturn

import arcade

# La posicion incial de la serpiente
CENTER_X, CENTER_Y = 150, 300


class Snake(arcade.SpriteList):

    def __init__(self) -> NoReturn:
        super().__init__()

        # Creamos las partes iniciales de la serpiente
        for i in range(3):
            self.append(self._create_sprite(CENTER_X - 10 * i, CENTER_Y))

    def _create_sprite(self, center_x: int, center_y: int) -> arcade.SpriteSolidColor:
         sprite_color = arcade.SpriteSolidColor(10, 10, arcade.color.GREEN)
         sprite_color.center_x = center_x
         sprite_color.center_y = center_y
         return sprite_color