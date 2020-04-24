import random as rd
from typing import List

# Constantes de movimiento
import arcade

R: int = 0
L: int = 1
U: int = 2
D: int = 3

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600

MOV_LIST: List[int] = [R, L, D, U]


def get_new_mov(last_mov: int) -> int:
    if last_mov in {R, L}:
        return rd.choice([U, D])
    elif last_mov in {U, D}:
        return rd.choice([R, L])


def get_mov_from_key(key: int, last_mov: int):
    if key == arcade.key.RIGHT and last_mov in {U, D}:
        return R
    elif key == arcade.key.LEFT and last_mov in {U, D}:
        return L
    elif key == arcade.key.UP and last_mov in {R, L}:
        return U
    elif key == arcade.key.DOWN and last_mov in {R, L}:
        return D
    else:
        return last_mov
