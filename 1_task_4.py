"""
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

from random import random

M1 = int(input("Введите нижнюю границу: "))
M2 = int(input("Введите верхнюю границу: "))
NUMB_1 = int(random() * (M2 - M1 + 1)) + M1
print(NUMB_1)

M3 = float(input("Введите нижнюю границу: "))
M4 = float(input("Введите верхнюю границу: "))
NUMB_2 = random() * (M4 - M3) + M3
print(round(NUMB_2, 2))

M5 = ord(input("Введите нижнюю границу: "))
M6 = ord(input("Введите верхнюю границу: "))
NUMB_3 = int(random() * (M6 - M5 + 1)) + M5
print(chr(NUMB_3))
