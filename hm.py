import datetime

# x, y = 10, 13
# h, m, c = 4, 37, 58
# # 1
# total_parts = int(((h * 60 * 60) + (m * 60) + c) // x + ((h * 60 * 60) + (m * 60) + c) // y)
# print(total_parts)
#
# # 2
# estimate_f = ((h * 60 * 60) + (m * 60) + c) % x
# estimate_f = x - estimate_f  # (estimate_f%1)*x сколько детали сделано в данный момент в пересчете на сек
#
# estimate_s = ((h * 60 * 60) + (m * 60) + c) % y
# estimate_s = y - estimate_s
#
# print(estimate_f)
# print(estimate_s)
#
# # 3
# if x < y:  # 1 изгат детали быстрее второго
#     numdetal_x = ((h * 60 * 60) + (m * 60) + c) // x  # сколько сделал деталей x
#     numdetal_y = ((h * 60 * 60) + (m * 60) + c) // y
#     how_many = numdetal_x - numdetal_y  # количество деталей которое нужно сделать что бы догнать
#     time = how_many * y - ((h * 60 * 60) + (m * 60) + c) % y # время, которое будет потрачено
#     time_h, time_m, time_s = time // 3600, time % 3600 // 60, time % 60
#     print(time_h, time_m, time_s, sep=':')
# elif x > y:
#     numdetal_x = ((h * 60 * 60) + (m * 60) + c) // x
#     numdetal_y = ((h * 60 * 60) + (m * 60) + c) // y
#     how_many = numdetal_y - numdetal_x
#     time = how_many * x - ((h * 60 * 60) + (m * 60) + c) % x
#     time_h, time_m, time_s = time // 3600, time%3600//60, time % 60
#     print(time_h, time_m, time_s, sep=':')
#
# # 4+5
# x, y = input().split()
# x = int(x)
# y = int(y)
# h, m, s = map(int, input().split(':'))


# 6
n = 924499
counter = 0  # пока 0  число непростое
for i in range(2, (n // 2) + 1):  # нужно проверить числа только от 2 до половины числа
    if n % i == 0:
        counter += 1  # число делится без остатка на какое то значит меняем каунтер
if counter == 1:
    print(f'{n} число простое')
else:
    print(f'{n} число непростое')
# # 7
# n = 1000000007
# b = int(n ** (0.5))
# counter = 0  # пока 0  число непростое
# for i in range(2, b + 1):  # нужно проверить числа только от 2 до половины числа
#     if n % i == 0:
#         counter += 1  # число делится без остатка на какое то значит меняем каунтер
# if counter == 1:
#     print(f'{n} число простое')
# else:
#     print(f'{n} число непростое')
# # 8
# n = 123456789
# count = 0  # каунт считает сколько шагов
# while n != 1:  # пока не равно 1 продолжаем шаги
#     if n % 2 == 0:  # если число четное то делим на 2
#         n = n / 2
#     else:
#         n = n * 3 + 1
#     count += 1
# print(count)
#
# # 9+10+11
N = 1000000
primes = [i for i in range(N + 1)]  # Создается список из значений от 0 до N включительно
primes[1] = 0  # Вторым элементом списка является единица, которую # не считают простым числом. Забиваем ее нулем
i = 2  # Начинаем с 3-го элемента
while i <= N:
    if primes[i] != 0:  # 0 - не простые числа (2 не 0)
        j = i + i  # Первое кратное ему будет в два раза больше 2+2=4
        while j <= N:  # п.3
            primes[j] = 0  # заменяем 4 на 0
            j = j + i  # переходим к следующему числу, # которое кратно i (оно на i больше) 4+2=6 возвращ к п 3
    i += 1  # как только j>100 переходим сюда и к 2 добавляем +1 =3
primes = [i for i in primes if i != 0]  # Избавляемся от всех нулей в списке
primes.sort()  # сортирую в порядке возрастания
print(primes)
print(primes[:10])  # беру от 0 до 10 отсортированный
print(primes[36])
print(primes[primes.index(37):primes.index(239)+1])
primes.sort(reverse=True)  # делаю обравтный список
print(primes)
#
# # 14
# # выводим поле
# field = [
#     ['.' for _ in range(3)]  # массив из точек 3 на 3
#     for _ in range(3)
# ]
#
#
# def print_field():
#     for row in field:
#         for cell in row:
#             print(cell, end=' ')
#         print()
#
#
# print_field()
#
#
# def player_move():
#     print('Please enter your move (row,col): ')
#     move = input()
#     row, col = move.split(',')
#     row, col = int(row) - 1, int(col) - 1
#
#     if field[row][col] != '.':
#         print('Cell is already taken')
#     else:
#         field[row][col] = 'X'
#
#
# # ход компьютера
# from random import randint
#
#
# def ai_move():
#     x = randint(0, 2)
#     y = randint(0, 2)
#     while field[x][y] != '.':
#         x = randint(0, 2)
#         y = randint(0, 2)
#     field[x][y] = 'O'
#
#
# WINS = [
#     [(0, 0), (0, 1), (0, 2)],  # 0-я строка
#     [(1, 0), (1, 1), (1, 2)],  # 1-я строка
#     [(2, 0), (2, 1), (2, 2)],  # 2-я строка
#     [(0, 0), (1, 0), (2, 0)],  # 0-й столбец
#     [(0, 1), (1, 1), (2, 1)],  # 1-й столбец
#     [(0, 2), (1, 2), (2, 2)],  # 2-й столбец
#     [(0, 0), (1, 1), (2, 2)],  # главная диагональ
#     [(0, 2), (1, 1), (2, 0)]  # побочная диагональ
# ]
#
#
# def check_win():
#     for option in WINS:
#         # print(f'Checking option {option}:')
#         values = []
#         for cell in option:
#             row, col = cell
#             value = field[row][col]
#             # print(f'\t-cell {cell} has value {value}')
#             values.append(value)
#         if values[0] == values[1] == values[2] != '.':
#             # print(f'All values are equal to {values[0]}, returning!')
#             return values[0]
#
#
# check_win()
#
# while True:
#     player_move()
#     print_field()
#     if check_win() == 'X':
#         print('You won!')
#         break
#     ai_move()
#     print_field()
#     if check_win() == 'O':
#         print('Computer wins!')
#         break
