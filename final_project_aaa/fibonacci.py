from itertools import islice
from functools import wraps
from typing import Callable, Iterable


def memoize(func: Callable) -> Callable:
    """
    Кэширует результат выполнения функции.
    Если функция с таким набором принимаемых аргументов
    уже выполнялась, то берется результат из кэша.
    """
    cache = dict()

    @wraps(func)
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return memoized_func


def fibonacci_iter() -> Iterable[int]:
    """Возвращает последовательность Фибоначчи (генератор)"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_generator_nth_element(gen: Iterable, index: int):
    """Возвращает значение по индексу из генератора"""
    return next(islice(gen, index, None))


@memoize
def fibonacci(n: int) -> int:
    """
    Возвращает число по индексу
    из последовательности Фибоначчи
    """
    return get_generator_nth_element(fibonacci_iter(), n)


if __name__ == '__main__':
    print(f'fib_20: {fibonacci(20)}')
    print(f'fib_6: {fibonacci(6)}')
