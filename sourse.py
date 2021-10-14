def greet():
    """Функция приветствия"""
    print("________________")
    print("Приветствую Тебя")
    print("_____в игре_____")
    print("Крестики нолики ")
    print("________________")
    print("формат ввода: x y")
    print("x - номер строки")
    print("y - номер столюца")


field = [[" "] * 3 for i in range(3)]
"""Задаем поле"""


def show():
    """Функция отображения поля"""
    print()
    print("   | 0 | 1 | 2 | ")
    print("_________________")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} |"
        print(row_str)
        print("_________________")
    print()


def ask():
    """Функци запрашивает у игрока координаты"""
    while True:
        cords = input("   Ваш ход: ").split()

        if len(cords) != 2:
            print("Введите 2 координаты!")
            continue

        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа!")
            continue

        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона!")
            continue

        if field[x][y] != " ":
            print("Клетка занята!")
            continue

        return x, y


def check_win():
    """Функция проверки выигрышных комбинаций"""
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Крестик!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл Нолик!")
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Крестик!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл Нолик!")
            return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
    if symbols == ["X", "X", "X"]:
        print("Выиграл Крестик!")
        return True
    if symbols == ["0", "0", "0"]:
        print("Выиграл Нолик!")
        return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][2 - i])
    if symbols == ["X", "X", "X"]:
        print("Выиграл Крестик!")
        return True
    if symbols == ["0", "0", "0"]:
        print("Выиграл Нолик!")
        return True

    return False
