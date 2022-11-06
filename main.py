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

# Создание поля NxN
field = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


# TODO
# pd.DataFrame(np.reshape((N, N)))


# Метод для рассчета количества клеток заданного процента
def calc_cell(cells_percent):
    n = N ** 2
    cells_count = n * cells_percent
    return int(cells_count)


# Заполнение поля пустыми значениями
# def start_init():
#     fo


# Метод для заполнения поля клетками в случайном порядке
def field_filling():
    blue = 0
    red = calc_cell(RED_PERCENT)
    # null = calc_cell(NULL_PERCENT)

    while blue != 0 & red != 0:
        c = random.randint(0, 4)  # рандомная колонка
        r = random.randint(0, 4)  # рандомный ряд

        if field[c][r] != 0:
            continue
        else:
            if blue != 0:
                field[c][r] = 1
                blue -= 1
            elif (blue == 0) and (red != 0):
                field[c][r] = 2
                red -= 1


# TODO delete
def print_field():
    for col in range(5):
        for row in range(5):
            print(field[col][row], end='')
        print('')


# Метод для рассчета счастлива клетка или нет
# def calc_lucky(matrix, i, j):

def get_unlucky():
    c = random.randint(0, 4)
    r = random.randint(0, 4)



def segregation():
    iterations_counter = 0
    while iterations_counter != ITERATIONS_NUM:
        field[random.randint(0, N - 1)][random.randint(0, N - 1)]
        iterations_counter += 1


if __name__ == '__main__':
    field_filling()
    print_field()
