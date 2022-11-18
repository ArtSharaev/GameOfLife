from config import *
import pygame


class Board:
    def __init__(self, dimensions, rendermode=0) -> None:
        self.size_x_px = dimensions[0]
        self.size_y_px = dimensions[1]
        self.size_x = dimensions[0] // CELL_SIZE
        self.size_y = dimensions[1] // CELL_SIZE
        self.matrix = []
        for _ in range(self.size_y):
            row = [0] * self.size_x
            self.matrix.append(row)
        self.rendermode = rendermode

    def set_alive(self, x, y) -> None:
        self.matrix[y][x] = 1

    @staticmethod
    def get_cell_coords(x_px, y_px) -> tuple:
        return x_px // CELL_SIZE, y_px // CELL_SIZE

    def matrix_update(self) -> None:
        """Обновление матрицы каждый игровой цикл"""
        temp = []
        for y in range(self.size_y):
            new_row = []
            for x in range(self.size_x):
                cell_value = self.cell_update(x, y)
                new_row.append(cell_value)
            temp.append(new_row)
        self.matrix = temp

    def cell_update(self, x, y) -> int:
        indexes = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
                   (1, 1), (1, 0), (1, -1), (0, -1)]
        counter = 0
        for i in indexes:
            ky, kx = i
            if (0 <= x + kx < self.size_x
                    and 0 <= y + ky < self.size_y):
                counter += self.matrix[y + ky][x + kx]
        if 2 <= counter <= 3 and self.matrix[y][x] == 1:
            return 1
        elif counter > 3 and self.matrix[y][x] == 1:
            return 0
        elif counter == 3 and self.matrix[y][x] == 0:
            return 1
        else:
            return 0

    def is_empty(self) -> bool:
        for row in self.matrix:
            if 1 in row:
                return False
        return True

    def change_rendermode(self) -> None:
        if self.rendermode:
            self.rendermode = 0
        else:
            self.rendermode = 1

    def render_cell(self, screen, x_px, y_px, cell_value) -> None:
        if cell_value:  # живая клетка
            pygame.draw.rect(screen, CELL_COLOR_1,
                             (x_px, y_px, CELL_SIZE, CELL_SIZE), 0)
            if self.rendermode:
                pygame.draw.rect(screen, CELL_BORDER_COLOR_1,
                                 (x_px, y_px, CELL_SIZE, CELL_SIZE), 1)
        else:  # пустая клетка
            pygame.draw.rect(screen, CELL_COLOR_0,
                             (x_px, y_px, CELL_SIZE, CELL_SIZE), 0)
            if self.rendermode:
                pygame.draw.rect(screen, CELL_BORDER_COLOR_0,
                                 (x_px, y_px, CELL_SIZE, CELL_SIZE), 1)

    def render(self, screen) -> None:
        x_px = y_px = 0
        for y in range(self.size_y):
            for x in range(self.size_x):
                self.render_cell(screen, x_px, y_px, self.matrix[y][x])
                x_px += CELL_SIZE
            y_px += CELL_SIZE
            x_px = 0
