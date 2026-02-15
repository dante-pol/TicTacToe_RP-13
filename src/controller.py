from __future__ import annotations

from src.display import *
from src.model.entities import Field
from src.model.constants import MARKER_EMPTY, MARKER_CROSS, MARKER_ZERO



class Referee:

    __field: Field

    def __init__(self, field: Field):
        self.__field = field

    def __check_win_by_row(self, marker: int) -> bool:

        for row in range(self.__field.rows):

            count_win = 0

            for column in range(self.__field.columns):

                if self.__field.cells[row][column].marker == marker:
                    count_win += 1

            if count_win == 3:
                return True

        return False


    def __check_win_by_column(self, marker: int) -> bool:

        for column in range(self.__field.columns):

            count_win = 0

            for row in range(self.__field.rows):

                if self.__field.cells[row][column].marker == marker:
                    count_win += 1

            if count_win == 3:
                return True

        return False

    def __check_win_by_diagonal(self, marker: int) -> bool:
        count_win_main = 0
        count_win_secondary = 0

        for i in range(self.__field.rows):

            if self.__field.cells[i][i].marker == marker:
                count_win_main += 1

            if self.__field.cells[i][self.__field.rows - 1 - i].marker == marker:
                count_win_secondary += 1

        if count_win_main == 3 or count_win_secondary == 3:
            return True

        return False

    def check_win(self, marker: int) -> bool:
        if self.__check_win_by_row(marker) or self.__check_win_by_column(marker) or self.__check_win_by_diagonal(marker):
            return True

        return False

    def check_draw(self) -> bool:

        for i in range(self.__field.rows):
            for j in range(self.__field.columns):

                if self.__field.cells[i][j].is_empty():
                    return False

        return True


class Game:

    VICTORY = 1
    DRAW = 0
    EMPTY = -1

    def __init__(self):
        self.__current_player = MARKER_EMPTY
        self.__status_gameplay = Game.EMPTY

        self.__field = Field(3, 3)
        self.__referee = Referee(self.__field)


    def set_up(self) -> None:
       self.__field.create()
       self.__current_player = MARKER_CROSS


    def try_make_move(self, x: int, y: int) -> bool | None:
        if self.__field.try_make_move(x, y, self.__current_player):

            if self.__referee.check_win(self.__current_player):
               self.__status_gameplay = Game.VICTORY
               return True

            elif self.__referee.check_draw():
                self.__status_gameplay = Game.DRAW
                return True

            return True

        return False


    def finish(self) -> None:
        if self.__status_gameplay == Game.VICTORY:
            self.show_field()
            show_info(f"{self.current_player} выиграли!!!")

        else:
            self.show_field()
            show_info(f"Ничья!!!")

        self.__field.reset()


    def swap(self) -> None:
        if self.__current_player == MARKER_CROSS:
            self.__current_player = MARKER_ZERO

        else:
            self.__current_player = MARKER_CROSS


    def validate_coord(self, coord) -> bool:
        if not coord.isdigit():
            return False

        if int(coord) > self.__field.rows or int(coord) > self.__field.columns:
            return False

        if int(coord) < 0:
            return False

        return True


    def show_field(self) -> str:
        return show_field(self.__field.cells)


    def __get_status_gameplay(self) -> int:
        return self.__status_gameplay


    def __get_current_player(self) -> int:
        return self.__current_player


    status_gameplay = property(__get_status_gameplay)
    current_player = property(__get_current_player)
