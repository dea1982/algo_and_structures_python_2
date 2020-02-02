"""
Задание 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""


import random


def median_search(lst, first, last):

    lst = lst.copy()
    ind = len(lst) // 2

    if first >= last:
        return lst[ind]

    pillar = lst[ind]
    i = first
    j = last

    while i <= j:

        while lst[i] < pillar:
            i += 1

        while lst[j] > pillar:
            j -= 1

        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

    if ind < i:
        lst[ind] = median_search(lst, first, j)

    elif j < ind:
        lst[ind] = median_search(lst, i, last)

    return lst[ind]


def merge_sort(arr):

    def merge(fst, snd):
        res = []
        i, j = 0, 0

        while i < len(fst) and j < len(snd):

            if fst[i] < snd[j]:
                res.append(fst[i])
                i += 1

            else:
                res.append(snd[j])
                j += 1

        res.extend(fst[i:] if i < len(fst) else snd[j:])

        return res

    def div_half(lst):

        if len(lst) == 1:
            return lst

        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]

        else:
            return merge(div_half(lst[:len(lst) // 2]),
                         div_half(lst[len(lst) // 2:]))

    return div_half(arr)


MIN_ITEM = 0
MAX_ITEM = 50
MIN_SIZE = 5
MAX_SIZE = 10

M = random.randint(MIN_SIZE, MAX_SIZE)
SIZE = 2 * M + 1

ARRAY = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(
    f'Сгенерирован массив из 2 * {M} + 1 = {SIZE}  элементов:',
    ARRAY,
    sep='\n')

MEDIAN = median_search(ARRAY, 0, len(ARRAY) - 1)
print(f'Медиана: {MEDIAN}')

print('Отсортированный массив: ', merge_sort(ARRAY), sep='\n')
if MEDIAN == merge_sort(ARRAY)[len(ARRAY) // 2]:
    print('\nВерно')
else:
    print('\nОшибка!!!')
