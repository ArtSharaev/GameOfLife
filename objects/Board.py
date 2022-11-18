from objects.Cell import Cell
from config import *
from pprint import pprint


class Board:
    def __init__(self, dimensions) -> None:
        self.size_x = dimensions[0]
        self.size_y = dimensions[1]
        self.cells_count_x = dimensions[0] // CELL_SIZE
        print(self.cells_count_x)
        self.cells_count_y = dimensions[1] // CELL_SIZE
        self.cells_array = []
        cur_x = cur_y = 0
        for i in range(self.cells_count_y):
            arr = []
            for j in range(self.cells_count_x):
                arr.append(Cell(self, (cur_x, cur_y), CELL_SIZE, BORDER_SIZE))
                cur_x += CELL_SIZE
            self.cells_array.append(arr)
            cur_y += CELL_SIZE
            cur_x = 0
        self.boolean_array = []
        for _ in range(self.cells_count_y):
            arr = [0] * self.cells_count_x
            self.boolean_array.append(arr)
        pprint(self.boolean_array)

    def update_array(self) -> None:
        pass

    def check_cell(self, x, y):
        indexes = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
                   (1, 1), (1, 0), (1, -1), (0, -1)]
        count = sum([self.boolean_array[y + i][x + j] for i, j in indexes])
        print(count)
        # if self.boolean_array[y - 1][x - 1]:
        #     counter += 1
        # if self.boolean_array[y - 1][x]:
        #     counter += 1
        # if self.boolean_array[y - 1][x + 1]:
        #     counter += 1
        # if self.boolean_array[y][x + 1]:
        #     counter += 1
        # if self.boolean_array[y + 1][x + 1]:
        #     counter += 1
        # if self.boolean_array[y + 1][x]:
        #     counter += 1
        # if self.boolean_array[y + 1][x - 1]:
        #     counter += 1
        # if self.boolean_array[y][x - 1]:
        #     counter += 1
        if counter >= 2 and self.boolean_array[y][x] == 1:
            return 1
        elif counter >= 3 and self.boolean_array[y][x] == 0:
            return 1
        else:
            return 0

    def get_cell_coords(self, x, y) -> tuple:
        return x // CELL_SIZE, y // CELL_SIZE

    def render(self, screen) -> None:
        for row in self.cells_array:
            for cell in row:
                cell.render(screen)
