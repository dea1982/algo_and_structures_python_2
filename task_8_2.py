"""
Задание 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""


# Вариант 1

from collections import Counter
from operator import itemgetter


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def walk(self, code, value):
        self.left.walk(code, value + ['0'])
        self.right.walk(code, value + ['1'])


class Leaf:
    def __init__(self, char):
        self.char = char

    def walk(self, code, value):
        code[self.char] = value


class HuffmanCodedString:
    def __init__(self, string):
        self.string = string
        self.code = {}
        self.node = self._make_node()
        self.node.walk(self.code, [])

    def _make_leaves(self, string):
        new_counted = {}
        for key, val in dict(Counter(string)).items():
            new_counted[Leaf(key)] = val
        return list(new_counted.items())

    def _make_node(self):
        items = self._make_leaves(self.string)
        while len(items) >= 2:
            left_leaf = items.pop()
            right_leaf = items.pop()
            leaf_count = left_leaf[1] + right_leaf[1]
            items.append(
                (MyNode(left=left_leaf[0], right=right_leaf[0]), leaf_count))
            items.sort(key=itemgetter(1), reverse=True)
        return items.pop()[0]

    def __str__(self):
        coded_string = []
        for i in self.string:
            coded_string += self.code[i] + [' ']
        return ''.join(coded_string)


if __name__ == '__main__':
    a = HuffmanCodedString('абра кадабра швабра')
    print(a.code)
    print(a)


# Вариант 2 (тоже самое, но функционально)


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def walk(self, code, value):
        self.left.walk(code, value + ['0'])
        self.right.walk(code, value + ['1'])


class Leaf:
    def __init__(self, char):
        self.char = char

    def walk(self, code, value):
        code[self.char] = ''.join(value)


def _make_leaves(obj: str):
    new_counted = {}
    for key, val in dict(Counter(obj)).items():
        new_counted[Leaf(key)] = val
    return list(new_counted.items())


def huff_encode(string_):
    items = _make_leaves(string_)
    while len(items) >= 2:
        left_leaf = items.pop()
        right_leaf = items.pop()
        leaf_count = left_leaf[1] + right_leaf[1]
        items.append(
            (MyNode(
                left=left_leaf[0], right=right_leaf[0]), leaf_count))
        items.sort(key=itemgetter(1), reverse=True)
    _node = items.pop()[0]
    code = {}
    _node.walk(code, [])
    print(code)
    for i in string_:
        print(code[i], end=' ')


if __name__ == '__main__':
    huff_encode('абра кадабра швабра')
