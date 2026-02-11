from src.controller import *
from src.display import *
from src.model.constants import *

def main():
    game = Game()

    game.set_up()
    print(show_field(game.get_field().get_cells()))

    print("Введите start чтобы начать игру >>")
    command = input()

    if command == COMMAND_START:

        is_game = True
        marker = MARKER_CROSS

        while is_game:

            print("Выберите номер column >>")
            x = int(input())

            print("Выберите номер row >>")
            y = int(input())

            if game.make_move(x, y, marker):
                show_info(f"{marker} выйграли")
                game.finish()
                is_game = False

            else:
                marker = MARKER_ZERO
                is_game = True

            print(show_field(game.get_field().get_cells()))




if __name__ == '__main__':
    main()






