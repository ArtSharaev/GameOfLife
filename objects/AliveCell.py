import pygame
from objects.Cell import Cell
from config import *


class AliveCell(Cell):
    def __init__(self, boardclass, coords, size, border_size) -> None:
        super().__init__(boardclass, coords, size, border_size)
        self.color = ALIVE_CELL_COLOR
        self.border_color = ALIVE_CELL_BORDER_COLOR

    def check_position(self):
        pass
