from __future__ import annotations
from src.model.constants import *

class Cell:

    __x: int
    __y: int
    __marker: int


    def __init__(self, x: int, y: int, marker = MARKER_EMPTY):
        self.__x = x
        self.__y = y
        self.__marker = marker


    def get_x(self) -> int:
        return self.__x


    def get_y(self) -> int:
        return self.__y


    def is_empty(self) -> bool:
        return self.__marker == MARKER_EMPTY


    def reset(self) -> None:
        self.__marker = MARKER_EMPTY


    def set_marker(self, marker: int) -> None:
        if marker != MARKER_ZERO and marker != MARKER_CROSS:
            raise ValueError(f"Not found marker: {marker}")

        self.__marker = marker


    def __get_marker(self) -> int:
        return self.__marker


    @staticmethod
    def copy(original: Cell) -> Cell:
        return Cell(original.__x, original.__y, original.__marker)


    marker = property(__get_marker)


class Field:

    __rows: int
    __columns: int
    __cells: list[list[Cell]]


    def __init__(self, rows: int, columns: int):
        self.__rows = rows
        self.__columns = columns

        self.__cells = []


    def let_move(self, x: int, y: int) -> bool:
        if x < 0 or x >= self.__rows: raise ValueError()
        if y < 0 or y >= self.__columns: raise ValueError()

        cell = self.__cells[x][y]

        if not cell.is_empty(): return False

        return True


    def create(self):

        for i in range(0, self.__rows, 1):
            self.__cells.append([])
            for j in range(0, self.__columns, 1):
                cell = Cell(i, j)
                self.__cells[i].append(cell)

    def reset(self):
        for i in range(0, self.__rows, 1):
            for j in range(0, self.__columns, 1):
                self.__cells[i][j].reset()


    def __get_rows(self) -> int:
        return self.__rows


    def __get_columns(self) -> int:
        return self.__columns


    def is_empty(self) -> bool:

        for x in range(self.__rows):
            for y in range(self.__columns):

                if not self.cells[x][y].is_empty():
                    return False

        return True


    @property
    def get_cells(self) -> list[list[Cell]]:
        cells = []

        for x in range(self.__rows):

            cells.append([])

            for y in range(self.__columns):

                cell = self.__cells[x][y]
                cells[x].append(cell.copy(cell))

        return cells


    rows = property(__get_rows)
    columns = property(__get_columns)
