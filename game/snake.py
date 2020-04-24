from typing import NoReturn, List, Tuple

import arcade

from game.movement import R, L, U, D, SCREEN_HEIGHT, SCREEN_WIDTH

# La posicion incial de la serpiente
CENTER_X, CENTER_Y = SCREEN_HEIGHT // 2, SCREEN_WIDTH // 2


class Snake(arcade.SpriteList):

    def __init__(self) -> NoReturn:
        super().__init__()

        self.direction: int = R
        self._direction_list: List[int] = 3 * [R]

        # Creamos las partes iniciales de la serpiente
        for i in range(3):
            self.append(self._create_sprite(CENTER_X - 10 * i, CENTER_Y))

    def eat_apple(self) -> NoReturn:
        # Añadimos una direccion a la cola
        last_dir: int = self._direction_list[-1]
        self._direction_list.append(last_dir)

        # La cola de la serpiente
        sprite_back: arcade.SpriteSolidColor = self[-1]

        center_x = sprite_back.center_x
        center_y = sprite_back.center_y

        if last_dir == R:
            center_x -= 10
        elif last_dir == L:
            center_x += 10
        elif last_dir == U:
            center_y -= 10
        elif last_dir == D:
            center_y += 10

        self.append(self._create_sprite(center_x, center_y))

    def update(self) -> NoReturn:
        # Añadimos la direccion y eliminamos el ultimo elemento
        self._direction_list.insert(0, self.direction)
        self._direction_list.pop()

        # Lista de posiciones
        part_pos: List[Tuple[float, float]] = []

        for direction, part in zip(self._direction_list, self):
            part = self._get_part_from_mov(part, direction)
            part.update()
            part_pos.append((part.center_x, part.center_y))

        # Si hay duplicados, error
        if len(part_pos) != len(set(part_pos)):
            print("Collision")
            raise ValueError("")

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

        if part.left < 0 or part.right > SCREEN_WIDTH - 1 or part.bottom < 0 or part.top > SCREEN_HEIGHT - 1:
            raise ValueError("Invalid movement")

        return part


    @staticmethod
    def _create_sprite(center_x: int, center_y: int) -> arcade.SpriteSolidColor:
         sprite_color = arcade.SpriteSolidColor(10, 10, arcade.color.GREEN)
         sprite_color.center_x = center_x
         sprite_color.center_y = center_y
         return sprite_color
