import time
from typing import NoReturn

from game.game_window import GameWindow
from game.movement import get_mov_from_key


class GameWindowManual(GameWindow):
    def on_update(self, delta_time: float) -> NoReturn:
        if not self.start_key:
            return

        time.sleep(0.1)

        try:
            self.snake.update()
            self.snake.update_animation()
        except:
            self.start_key = False

    def on_key_press(self, symbol: int, modifiers: int):
        self.start_key = True

        self.snake.direction = get_mov_from_key(symbol, self.snake.direction)
