"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.
"""

try:
    NUMB = int(input("Введите номер буквы: "))
    print(f"Введёному номеру соответствует буква: {chr(ord('a') + NUMB - 1)}")
except:
    print("Вы ввели букву!")
