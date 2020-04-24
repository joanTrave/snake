import time
from typing import NoReturn

from game.game_window import GameWindow
from game.movement import get_mov_from_key, DELTA_TIME


class GameWindowManual(GameWindow):
    def on_update(self, delta_time: float) -> NoReturn:
        if not self.start_key:
            return

        time.sleep(DELTA_TIME)

        super().update(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):
        self.start_key = True

        self.snake.direction = get_mov_from_key(symbol, self.snake.direction)
