# Крестики-нолики
# ● Контекст
# Вероятнее всего, вы с детства знакомы с этой игрой. Пришло время реализовать её. Два игрока по очереди ставят крестики
# и нолики на игровое поле. Игра завершается когда кто-то победил, либо наступила ничья, либо игроки отказались
# играть.
# ● Задача
# Написать игру в “Крестики-нолики”. Можете использовать любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.

def play_the_game(play_field):
    print("Начинает тот, кто выбрал крестики.")
    sign = 'X'
    while True:
        if (play_field[0][0] == play_field[0][1] == play_field[0][2] != "*"
                or play_field[1][0] == play_field[1][1] == play_field[1][2] != "*"
                or play_field[2][0] == play_field[2][1] == play_field[2][2] != "*"
                or play_field[0][0] == play_field[1][0] == play_field[2][0] != "*"
                or play_field[0][2] == play_field[1][2] == play_field[2][2] != "*"
                or play_field[0][1] == play_field[1][1] == play_field[2][1] != "*"
                or play_field[0][0] == play_field[1][1] == play_field[2][2] != "*"
                or play_field[0][2] == play_field[1][1] == play_field[2][0] != "*"
                or ("*" not in play_field[0] and "*" not in play_field[1] and "*" not in play_field[2])):
            print(" Игра окончена!")
            print_field(play_field)
            break
        else:
            coordinates = ask_and_check_coordinates(play_field)
            if coordinates == '777':
                print(" Игра окончена!")
                print_field(play_field)
                break
            elif sign == "X":
                print("Сейчас ставим крестик")
                play_field[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = "X"
                sign = "0"
                print_field(play_field)
            elif sign == '0':
                print("Сейчас ставим нолик")
                play_field[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = "0"
                sign = "X"
                print_field(play_field)


def ask_and_check_coordinates(play_field):
    coordinates = input("Если хотите продолжить игру, введите номер ряда и номер места (без пробела).\n"
                        "Если хотите прервать игру, введите 777: ")
    while True:
        if coordinates == '777':
            break
        elif (len(coordinates) != 2
                or not coordinates.isdigit()
                or not 0 < int(coordinates[0]) < 4
                or not 0 < int(coordinates[1]) < 4):
            coordinates = input("Некорректный ввод. Введите номер ряда и номер места (без пробела): ")
        elif play_field[int(coordinates[0]) - 1][int(coordinates[1]) - 1] != '*':
            coordinates = input("Это поле уже занято. Введите другие номер ряда и номер места (без пробела): ")
        else:
            break
    return coordinates


def print_field(play_field):
    for i in range(0, 3):
        print(play_field[i][0] + " " + play_field[i][1] + " " + play_field[i][2])


if __name__ == '__main__':
    play_field: list[list[str]] = [['*','*','*'],['*','*','*'],['*','*','*']]
    play_the_game(play_field)










