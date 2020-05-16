import operator
from typing import Iterable, Callable
from functools import partial


def sum_elements(x: Iterable, y: Iterable) -> Iterable:
    return map(operator.add, x, y)


def min_zip(x: Iterable, y: Iterable) -> Iterable:
    return map(min, zip(x, y))


get_sum_rgb = partial(min_zip, (255, 255, 255))


def elem_func(func: Callable, x: Iterable) -> Iterable:
    return map(func, x)
