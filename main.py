from src.controller import *
from src.model.constants import *

def main():
    game = Game()

    print("Введите start чтобы начать игру >>")
    command = input()

    if command == COMMAND_START:

        game.set_up()
        is_game = True

        while is_game:
            game.show_field()

            print("Выберите номер row >>")
            x = input()

            print("Выберите номер column >>")
            y = input()

            if game.validate_coord(x) and game.validate_coord(y):

                if game.try_make_move(int(x), int(y)):

                    if game.status_gameplay == Game.VICTORY:
                        game.finish()
                        is_game = False

                    elif game.status_gameplay == Game.DRAW:
                        game.finish()
                        is_game = False

                    else:
                        game.swap()

                else:
                    print("Клетка заполнена!!!")


            else:
                print("Не корректный ввод!!!")

    else:
        print("Не корректный ввод!!!")


if __name__ == '__main__':
    main()






