"""
Задание 5.	Пользователь вводит две буквы. Определить,
на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

import sys

try:
    PARAM_1 = ord(input('1-я буква: '))
    PARAM_2 = ord(input('2-я буква: '))
except BaseException:
    print('Введите буквы')
    sys.exit(1)

if PARAM_1 == PARAM_2:
    print('Введены одинаковые буквы ')
    sys.exit(1)

PARAM_1 = PARAM_1 - ord('a') + 1
PARAM_2 = PARAM_2 - ord('a') + 1

print(f"Позиции: {PARAM_1} и {PARAM_2}")
print(f"Между буквами символов: {abs(PARAM_1 - PARAM_2) - 1}")
