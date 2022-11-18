import pygame
from config import *


class Cell:
    def __init__(self, boardclass, coords, size, border_size) -> None:
        self.boardclass = boardclass
        self.x, self.y = coords[0], coords[1]
        self.color = CELL_COLOR
        self.border_color = CELL_BORDER_COLOR
        self.size = size
        self.border_size = border_size

    def render(self, screen) -> None:
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.size, self.size), 0)
