from constants import *

class Cell:

    class RecordCell:

        __x: int
        __y: int
        marker: str

        def __init__(self, x: int, y: int, marker: str):

            self.__x = x
            self.__y = y
            self.__marker = marker


    __x: int
    __y: int

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
        self.__marker = MARKER_EMPTY

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def is_empty(self) -> bool:
        return self.__marker == MARKER_EMPTY

    def set_marker(self, marker: int) -> None:
        if marker != MARKER_ZERO and marker != MARKER_CROSS:
            raise ValueError(f"Not found marker: {marker}")

        self.__marker = marker

    def reset(self) -> None:
        self.__marker = MARKER_EMPTY


    def get_record(self) -> RecordCell:
        return Cell.RecordCell(self.__x, self.__y, self.__marker)


class Field:

    __rows: int
    __columns: int
    __cells: list[list[Cell]]

    def __init__(self, rows: int, columns: int):
        self.__rows = rows
        self.__columns = columns

        self.__cells = []


    def get_rows(self):
        return self.__rows

    def get_columns(self):
        return self.__columns


    def try_make_move(self, x: int, y: int, marker) -> bool:
        if x < 0 or x >= self.__rows: raise ValueError()
        if y < 0 or y >= self.__columns: raise ValueError()

        if marker != MARKER_CROSS and marker != MARKER_ZERO: raise ValueError()

        cell = self.__cells[x][y]

        if not cell.is_empty(): return False

        cell.set_marker(marker)

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


    def get_cell(self) -> list[list[Cell.RecordCell]]:

        new_cell = []

        for x in range(self.__rows):
            new_cell.append([])
            for y in range(self.__columns):
                cell = self.__cells[x][y]

                new_cell[x].append(Cell.get_record(cell))

        return new_cell



