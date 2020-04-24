import random as rd
from typing import List

# Constantes de movimiento
R: int = 0
L: int = 1
U: int = 2
D: int = 3

MOV_LIST: List[int] = [R, L, D, U]


def get_new_mov(last_mov: int) -> int:
    if last_mov in {R, L}:
        return rd.choice([U, D])
    elif last_mov in {U, D}:
        return rd.choice([R, L])
