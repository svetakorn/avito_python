import operator
from typing import Iterable
from functools import partial


def sum_elements(x: Iterable, y: Iterable) -> Iterable:
    """Поэлементно складывает два объекта"""
    return map(operator.add, x, y)


def min_zip(x: Iterable, y: Iterable) -> Iterable:
    """
    Совмещает два объекта с помощью zip,
    а потом находит минимальное значение в каждой паре
    """
    return map(min, zip(x, y))


get_sum_rgb = partial(min_zip, (255, 255, 255))
