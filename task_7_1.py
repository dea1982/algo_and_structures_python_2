"""
Задание 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""


import random


def bubble_sort(lst):
    n = 1

    while n < len(lst):
        count = 0

        for i in range(len(lst) - 1 - (n - 1)):

            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                count += 1

        if count == 0:
            break

        n += 1


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
ARRAY = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('Массив:', ARRAY, sep='\n')
bubble_sort(ARRAY)
print('После сортировки:', ARRAY, sep='\n')
