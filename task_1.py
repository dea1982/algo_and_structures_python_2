"""
Задание 1. Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
"""

NUMBERS = int(input("Введите целое трехзначное число: "))

# отбросить остаток
RESULT_A = NUMBERS // 100
# остаток от деления числа
RESULT_B = (NUMBERS // 10) % 10
# остаток от деления числа
RESULT_C = NUMBERS % 10

print(f"Сумма = {RESULT_A + RESULT_B + RESULT_C}")
print(f"Произведение = {RESULT_A * RESULT_B * RESULT_C}")
