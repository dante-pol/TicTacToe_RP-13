from __future__ import annotations
from model.entities import Field
from src.model.constants import MARKER_EMPTY


class Referee:

    __field: Field

    def __init__(self, field: Field):
        self.__field = field

    def check_win(self, marker) -> bool:

        if self.__check_win_by_row() == True or self.__check_win_by_column() == True or self.__check_win_by_diagonal() == True:

            return True

        return False

    def check_draw(self, marker) -> bool:

        if not self.check_win() == False and not self.__field.try_make_move():

            return False

        return True

    def __check_win_by_row(self, field) -> bool:

        for cell in range(0, 3, 1):

            if field[cell][0] == field[cell][1] == field[cell][2] != MARKER_EMPTY:

                return True

        return False

    def __check_win_by_column(self, field) -> bool:

        for col in range(0, 3, 1):

            if field[0][col] == field[1][col] == field[2][col] != MARKER_EMPTY:

                return True

        return False

    def __check_win_by_diagonal(self, field) -> bool:

        if field[0][0] == field[1][1] == field[2][2] != MARKER_EMPTY or field[0][2] == field[1][1] == field[2][0] != MARKER_EMPTY:

            return True

        return False


class Game:

    def __init__(self):
        self.__current_player = MARKER_EMPTY

        self.__field = Field(3, 3)
        self.__referee = Referee(self.__field)


    def set_up(self) -> None:
        pass

    def make_move(self, x, y) -> bool | str:

        player = self.__current_player

        if not player.try_make_move(): return False

        player.make_move()


        winner = self.__referee.check_win()

        if winner != MARKER_EMPTY:

            return f"Player {player} wins!"


        if self.__referee.check_draw():

            return f"Draw!"

        return True


    def finish(self) -> None:
        pass

