from sourse import *

greet()
"""Запускаем функцию приветствия"""

num = 0
while True:
    """запускаем бесконечный цикл со счетчиком ходов"""
    num += 1
    show()
    """запускаем функцию отображения поля на каждом шаге"""

    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = ask()
    """передаем функции ask введенные координаты"""
    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        """проверяем наличие выигрышных комбинаций на каждом шаге"""
        break

    if num == 9:
        """если количество шагов доходит до максимального значения клеток - игра заканчивается"""
        print("Ничья!")
        break