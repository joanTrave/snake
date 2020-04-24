import random as rd
import time
from typing import NoReturn

from game.game_window import GameWindow
from game.movement import get_new_mov


class GameWindowAutomatic(GameWindow):

    def on_update(self, delta_time: float) -> NoReturn:
        self.start_key = True

        time.sleep(0.1)

        # AQUI EMPIEZA LA LOGICA ---------------------------------------------------------------------------------------
        if rd.choice(6*[False] + 4*[True]):
            self.snake.direction = get_new_mov(self.snake.direction)

        # --------------------------------------------------------------------------------------------------------------
        # NO TOCAR ESTA LINEA
        super().update(delta_time)
