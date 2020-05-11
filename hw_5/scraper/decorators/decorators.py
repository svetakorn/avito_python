import time
import datetime
import functools
from typing import Callable
from scraper.decorators.logger import logger


def timer(func: Callable) -> Callable:
    """Выводит время выполнения декорируемой функции"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        logger.write_log(get_current_time(), func.__name__, '{0:.6f}'.format(run_time))
        return value
    return wrapper_timer


def get_current_time() -> str:
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def memoize(func: Callable) -> Callable:
    """
    Кэширует результат выполнения функции.
    Если функция с таким набором принимаемых аргументов уже выполнялась,
    то берется результат из кэша.
    """
    cache = dict()

    @functools.wraps(func)
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return memoized_func


@memoize
def sveta(num: int):
    return num ^ 2


a = sveta(3)
b = sveta(3)
c = sveta(4)


