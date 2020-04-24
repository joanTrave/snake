from typing import NoReturn, List

import arcade

# La posicion incial de la serpiente
from game.movement import R, L, U, D

CENTER_X, CENTER_Y = 150, 300


class Snake(arcade.SpriteList):

    def __init__(self) -> NoReturn:
        super().__init__()

        self.direction: int = R
        self._direction_list: List[int] = 8 * [R]

        # Creamos las partes iniciales de la serpiente
        for i in range(8):
            self.append(self._create_sprite(CENTER_X - 10 * i, CENTER_Y))

    def update(self) -> NoReturn:
        print(self._direction_list)
        # Añadimos la direccion y eliminamos el ultimo elemento
        self._direction_list.insert(0, self.direction)
        self._direction_list.pop()

        for direction, part in zip(self._direction_list, self):
            part = self._get_part_from_mov(part, direction)
            part.update()

    @staticmethod
    def _get_part_from_mov(part: arcade.SpriteSolidColor, mov: int) -> arcade.SpriteSolidColor:
        if mov == R:
            part.change_y = 0
            part.change_x = 10
        elif mov == L:
            part.change_y = 0
            part.change_x = -10
        elif mov == U:
            part.change_y = 10
            part.change_x = 0
        elif mov == D:
            part.change_y = -10
            part.change_x = 0
        else:
            raise ValueError("Invalid movement")
        return part


    @staticmethod
    def _create_sprite(center_x: int, center_y: int) -> arcade.SpriteSolidColor:
         sprite_color = arcade.SpriteSolidColor(10, 10, arcade.color.GREEN)
         sprite_color.center_x = center_x
         sprite_color.center_y = center_y
         return sprite_color
