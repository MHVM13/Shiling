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


# Функция для заполнения поля клетками в случайном порядке
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


# Функция для проверки является ли эта клетка несчастливой
def is_unlucky(index_i, index_j):
    the_same_counter = 0

    if field[index_i, index_j] != 0:  # Пустая клетка
        for i in range(0, N):
            for j in range(0, N):
                if (abs(index_i - i) == 1 or abs(index_i - i) == 0) and (
                        abs(index_j - j) == 1 or abs(index_j - j) == 0):
                    if i != index_i or j != index_j:  # Чтобы не считать саму себя
                        if field[i][j] == field[index_i][index_j]:
                            the_same_counter += 1

        if the_same_counter < FOR_HAPPY:
            return True

    return False


# Функция для проверки всего поля, на наличие несчастливых клеток
def is_there_unlucky():
    for i in range(N):
        for j in range(N):
            if is_unlucky(i, j):
                return True

    return False


# Случайный поиск несчастливой клетки
def get_unlucky():
    while True:
        # Генерация индексов произвольной клетки
        rand_i = random.randint(0, N - 1)
        rand_j = random.randint(0, N - 1)

        if is_unlucky(rand_i, rand_j):
            return rand_i, rand_j


# Поиск пустых клеток и создание списка из них
def find_empty():
    empty_cells = list()

    for i in range(N):
        for j in range(N):
            if field[i][j] == 0:
                empty_cells.append((i, j))

    return empty_cells


# Поиск пустой клетки
def get_empty():
    empty_cells = find_empty()
    rand_value = random.randint(0, len(empty_cells) - 1)
    return empty_cells[rand_value][0], empty_cells[rand_value][1]


# Модель рассовой сегрегации
def segregation(iterations_num):
    iterations_counter = 0

    # Выполняется пока не достигнется определенное количество итераций или пока не оставнется несчастливых клеток
    while iterations_counter != iterations_num and is_there_unlucky():
        print(f'Progress: {iterations_counter}')

        unlucky_i, unlucky_j = get_unlucky()
        empty_i, empty_j = get_empty()

        # Перемещаем несчастную клетку в свободное место
        field[empty_i][empty_j] = field[unlucky_i][unlucky_j]
        field[unlucky_i][unlucky_j] = 0

        iterations_counter += 1

    get_graph()


# MAIN
field_filling()
segregation(int(input('Введите количество итераций: ')))
