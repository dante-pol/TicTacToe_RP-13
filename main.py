from src.controller import *
from src.display import *
from src.model.constants import *

def main():
    game = Game()

    print("Введите start чтобы начать игру >>")
    command = input()

    if command == COMMAND_START:

        game.set_up()
        is_game = True

        while is_game:
            print(show_field(game.field.cells))

            print("Выберите номер row >>")
            x = input()


            print("Выберите номер column >>")
            y = input()

            if game.validate_coord(x) and game.validate_coord(y):

                result = game.try_end_game(int(x), int(y))

                if result:

                    if game.status_gameplay == Game.VICTORY:

                        game.finish()
                        is_game = False

                    elif game.status_gameplay == Game.DRAW:

                        game.finish()
                        is_game = False

                elif result is None:
                    print("Клетка заполнена!!!")

                else:
                    game.swap()

            else:
                print("Не корректный ввод!!!")

    else:
        print("Не корректный ввод!!!")


if __name__ == '__main__':
    main()






