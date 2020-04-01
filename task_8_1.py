"""
Задание 1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

from hashlib import sha1

STRING = input('Введите строку: ')

STR_LEN = len(STRING)
SUB_LEN = 1

SUB_STRINGS = []

while STR_LEN > 1:
    for i in range(STR_LEN):
        sub = sha1(STRING[i:i + SUB_LEN].encode('utf-8')).hexdigest()
        if sub not in SUB_STRINGS:
            SUB_STRINGS.append(sub)
    SUB_LEN += 1
    STR_LEN -= 1

print(f'В строке "{STRING}" {len(SUB_STRINGS)} уникальных подстрок')
