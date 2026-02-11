from __future__ import annotations
from model.entities import Field
from src.model.constants import MARKER_EMPTY


class Referee:

    __field: Field

    def __init__(self, field: Field):
        self.__field = field

    def __check_win_by_row(self, marker: int) -> bool:
        is_win = False

        for row in range(self.__field.get_rows()):
            for column in range(self.__field.get_columns()):

                if self.__field.get_cells()[row][column] == marker:
                    is_win = True

                else:
                    is_win = False

            if is_win:
                return True

        return False


    def __check_win_by_column(self, marker: int) -> bool:
        is_win = False

        for column in range(self.__field.get_columns()):
            for row in range(self.__field.get_rows()):

                if self.__field.get_cells()[row][column] == marker:
                    is_win = True

                else:
                    is_win = False

            if is_win:
                return True

        return False

    def __check_win_by_diagonal(self, marker: int) -> bool:
        is_win = False

        for row in range(self.__field.get_rows()):
            for column in range(self.__field.get_columns()):

                if self.__field.get_cells()[row][row] == marker:
                    is_win = True

                elif self.__field.get_cells()[row][self.__field.get_rows() - 1 - row] == marker:
                    is_win = True

                else:
                    is_win = False

            if is_win:
                return True

        return False

    def check_win(self, marker: int) -> bool:
        if self.__check_win_by_row(marker) or self.__check_win_by_column(marker) or self.__check_win_by_diagonal(marker):
            return True

        return False

    def check_draw(self, marker: int) -> bool:
        if not self.__check_win_by_row(marker) and not self.__check_win_by_column(marker) and not self.__check_win_by_diagonal(marker):
            return True

        return False


class Game:

    def __init__(self):
        self.__current_player = MARKER_EMPTY

        self.__field = Field(3, 3)
        self.__referee = Referee(self.__field)


    def set_up(self) -> None:
        pass

    def make_move(self, x, y) -> None:
        pass

    def finish(self) -> None:
        pass

