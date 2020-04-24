import random as rd
import time
from typing import NoReturn

from game.game_window import GameWindow
from game.movement import get_new_mov, DELTA_TIME


class GameWindowAutomatic(GameWindow):

    def on_update(self, delta_time: float) -> NoReturn:
        self.start_key = True

        time.sleep(DELTA_TIME)

        self.snake.direction = self._get_best_movement()

        # NO TOCAR ESTA LINEA
        super().update(delta_time)

    def _get_best_movement(self) -> int:
        """
        En este metodo se devuelve el mejor movimiento dado el estado actual del tablero

        Por defecto se devuelve un random
        """
        return get_new_mov(self.snake.direction) if rd.choice(6*[False] + 4*[True]) else self.snake.direction
