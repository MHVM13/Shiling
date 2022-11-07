# Для импортирования библиотек
import random
import pandas as pd
import numpy as np

# TASK
# Реализовать модель Шеллинга (модель расовой
# сегрегации)
#
# Дан квадрат n x n. 45% клеток синие, 45% клеток
# красные, 10% клеток пустые. Начальное заполнение в
# случайном порядке.
#
# Клетка «счастлива» если у нее 2 или более соседа
# одного с ней цвета. Соседи – это 8 клеток вокруг данной.
#
# Моделирование: выбрать случайным образом
# «несчастную» клетку и переместить ее в случайно
# выбранную пустую клетку.
#
# Вывести квадраты через данное некоторое количество
# шагов иллюстрирующее расовую сегрегацию.


# !!!!
# blue = 1 red = 2 null = 0

N = 5  # TODO input('Введете сторону квадрата: ')
ITERATIONS_NUM = 5  # TODO input('Введете количество итераций: ')
BLUE_PERCENT = 0.45
RED_PERCENT = 0.45
NULL_PERCENT = 0.10
HAPPY_CELLS_COUNTER = 2  # количество клеток-соседей для того, чтобы выбранная клетка была счаслива

# Создание пустого поля NxN
field = np.zeros((N, N), dtype=int)


# Метод для рассчета количества клеток заданного процента
def calc_cell(cells_percent):
    n = N ** 2
    cells_count = n * cells_percent
    return int(cells_count)


# Метод для заполнения поля клетками в случайном порядке
def field_filling():
    blue = calc_cell(BLUE_PERCENT)
    red = calc_cell(RED_PERCENT)

    while blue != 0 or red != 0:
        i = random.randint(0, N - 1)  # рандомная колонка
        j = random.randint(0, N - 1)  # рандомный ряд

        if field[i][j] != 0:
            continue
        else:
            if blue != 0:
                field[i][j] = 1
                blue -= 1
            elif (blue == 0) and (red != 0):
                field[i][j] = 2
                red -= 1


# Поиск несчастливой клетки
def get_unlucky():
    the_same_counter = 0  # количество соседей похожих на выбранную клетку

    while True:
        i = 0  # TODO random.randint(0, N-1)
        j = 0  # TODO random.randint(0, N-1)

        # Проверка ближайщих соседей
        # TODO проверка на выходы за границы или выброс исключения
        if field[i - 1][j - 1] == field[i][j]: the_same_counter += 1
        if field[i][j - 1] == field[i][j]: the_same_counter += 1
        if field[i - 1][j + 1] == field[i][j]: the_same_counter += 1
        if field[i + 1][j] == field[i][j]: the_same_counter += 1
        if field[i + 1][j + 1] == field[i][j]: the_same_counter += 1
        if field[i][j + 1] == field[i][j]: the_same_counter += 1
        if field[i - 1][j + 1] == field[i][j]: the_same_counter += 1
        if field[i - 1][j] == field[i][j]: the_same_counter += 1

        if the_same_counter >= 2:
            return i, j


# Поиск пустой клетки
def get_empty():
    for i in range(0, N - 1):
        for j in range(0, N - 1):
            if field[i][j] == 0:
                return i, j


# Модель рассовой сегрегации
def segregation():
    iterations_counter = 0

    while iterations_counter != ITERATIONS_NUM:
        unlucky_i, unlucky_j = get_unlucky()
        empty_i, empty_j = get_empty()

        # Перемещаем несчастную клетку в свободное место
        field[empty_i][empty_j] = field[unlucky_i][unlucky_j]
        field[unlucky_i][unlucky_j] = 0

        iterations_counter += 1


# MAIN
field_filling()
print(field)
print('\n')
segregation()
print(field)
