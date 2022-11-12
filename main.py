import random
import numpy as np
import matplotlib.pyplot as plt

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

N = int(input('Введете сторону квадрата: '))
BLUE_PERCENT = 0.45
RED_PERCENT = 0.45
FOR_HAPPY = 2  # количество клеток-соседей для того, чтобы выбранная клетка была счаслива

# Создание пустого поля NxN
field = np.zeros((N, N), dtype=int)


# Вывод графика
def get_graph():
    plt.imshow(field, cmap='magma')
    plt.show()


# Метод для рассчета количества клеток заданного процента
def calc_cells(cells_percent):
    n = N ** 2
    cells_num = n * cells_percent
    return int(cells_num)


# Метод для заполнения поля клетками в случайном порядке
def field_filling():
    blue = calc_cells(BLUE_PERCENT)
    red = calc_cells(RED_PERCENT)

    while blue != 0 or red != 0:
        # Генерация случаных индексов
        i = random.randint(0, N - 1)  # случайная колонка
        j = random.randint(0, N - 1)  # случайная ряд

        if field[i][j] != 0:
            continue
        else:
            if blue != 0:
                field[i][j] = 1
                blue -= 1
            elif (blue == 0) and (red != 0):
                field[i][j] = 2
                red -= 1

    get_graph()


# Поиск несчастливой клетки
def get_unlucky():
    while True:
        the_same_counter = 0  # количество соседей похожих на выбранную клетку

        # Генерация индексов произвольной клетки
        rand_i = random.randint(0, N - 1)
        rand_j = random.randint(0, N - 1)

        if field[rand_i, rand_j] != 0:
            for i in range(0, N):
                for j in range(0, N):
                    if i != rand_i and j != rand_j:  # Попали на ту же клетку
                        if abs(rand_i - i) == 1 and abs(rand_j - j) == 1:
                            if field[i][j] == field[rand_i][rand_j]:
                                the_same_counter += 1

            if the_same_counter < FOR_HAPPY:
                return rand_i, rand_j


# Поиск пустой клетки
def get_empty():
    for i in range(0, N):
        for j in range(0, N):
            if field[i][j] == 0:
                return i, j


# Модель рассовой сегрегации
def segregation(iterations_num):
    iterations_counter = 0

    while iterations_counter != iterations_num:
        unlucky_i, unlucky_j = get_unlucky()
        empty_i, empty_j = get_empty()

        # Перемещаем несчастную клетку в свободное место
        field[empty_i][empty_j] = field[unlucky_i][unlucky_j]
        field[unlucky_i][unlucky_j] = 0

        get_graph()
        iterations_counter += 1


# MAIN
field_filling()
segregation(int(input('Введите количество итераций: ')))