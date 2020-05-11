import time
import datetime
import os
import functools
from typing import Callable

logs_folder = os.path.join(os.path.dirname(__file__), '../logs')


class LogWriterPipeline:
    """Содержит пайплайн сохранения логов"""
    def __init__(self):
        self.current_time_str = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        self.file = None

    def open_logs(self):
        if self.file is None:
            self.file = open(f'{logs_folder}/logs_start_{self.current_time_str}.txt', 'a')

    def close_logs(self):
        self.file.close()
        self.file = None

    def write_log(self, end_time, func_name, run_time):
        if self.file is not None:
            self.file.write('{0}  |  {1}  |  {2}\n'.format(end_time, func_name, run_time))


logger = LogWriterPipeline()


def timer(func: Callable) -> Callable:
    """Выводит время выполнения декорируемой функции"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        logger.write_log(get_current_time(), func.__name__, '{0:.8f}'.format(run_time))
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
