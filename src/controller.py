from __future__ import annotations

from model.entities import Field
from src.model.constants import MARKER_ZERO
from src.model.constants import MARKER_CROSS
from src.model.constants import MARKER_EMPTY


class Referee:

    __field: Field

    def __init__(self, field: Field):
        self.__field = field

    def check_win(self) -> bool:

        if self.__check_win_by_row() or self.__check_win_by_column() or self.__check_win_by_diagonal() or self.__check_win_secondary_diagonal():
            return True

        return False


    def check_draw(self) -> bool:

        for row in self.__field:
            for elem in row:

                if elem == MARKER_EMPTY or elem == '': return False

                if elem not in (MARKER_CROSS, MARKER_ZERO):  return False


        return True


    def __check_win_by_row(self) -> bool:

        for row in self.__field.get_rows():
            new_row = row[0]

            if  new_row == '':
                continue
            if new_row not in (MARKER_ZERO, MARKER_CROSS):
                return False
            is_win = True
            for elem in row:
                if elem != new_row:
                    is_win = False
                    break

            if is_win:
                return True

        return False


    def __check_win_by_column(self) -> bool:

        for column in range(len(self.__field.get_columns())):
            new_column = self.__field[0][column]

            if new_column == '':
                continue
            if new_column not in (MARKER_ZERO, MARKER_CROSS):
                return False

            is_win = True
            for elem in range(len(self.__field.get_columns())):
                if new_column != self.__field[elem][column]:
                    is_win = False
                    break

            if is_win:
                return True

        return False


    def __check_win_by_diagonal(self) -> bool:

        new_diagonal = self.__field[0][0]

        if new_diagonal == '':  return False

        if new_diagonal not in (MARKER_ZERO, MARKER_CROSS):  return False

        is_win = True

        for i in range(len(self.__field.get_rows())):
            for j in range(len(self.__field.get_columns())):
                if new_diagonal != self.__field[i][i]:
                    is_win = False
                    break

        if is_win:
            return True

        return False

    def __check_win_secondary_diagonal(self) -> bool:

        length = len(self.__field)

        new_sec_diagonal = self.__field[0][length - 1]

        if new_sec_diagonal == '': return False

        if new_sec_diagonal not in (MARKER_ZERO, MARKER_CROSS): return False

        is_win = True

        for i in range(length):
            if new_sec_diagonal != self.__field[i][length - 1- i]:
                is_win = False
                break

        if is_win:
            return True

        return False


class Game:

    def __init__(self):
        self.__current_player = MARKER_EMPTY

        self.__field = Field(3, 3)
        self.__referee = Referee(self.__field)


    def set_up(self) -> None:

        self.__field.create()
        self.__current_player = MARKER_CROSS

    def make_move(self, x: int, y: int, marker) -> None:

        self.__field.try_make_move()

    def finish(self) -> None:
        pass

