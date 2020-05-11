import typing
from collections import deque
import requests
from scraper.pipelines import CSVPipeline, JLPipeline, MongoPipeline


def start(start_url: str, callback: typing.Callable, out_path: str, out_format: str, progress_mode: str):
    start_task = (start_url, callback)
    tasks = deque([start_task])

    obj_pipeline = get_pipeline(out_path, out_format, progress_mode)
    obj_pipeline.open_spider()

    try:
        while tasks:
            url, callback = tasks.popleft()
            resp = requests.get(url)

            for result in callback(resp):
                if isinstance(result, dict):
                    obj_pipeline.process_item(result)
                    print_progress(out_path, progress_mode, tasks)
                else:
                    tasks.append(result)
    finally:
        obj_pipeline.close_spider()


def print_progress(out_path, progress_mode, tasks):
    """Выводит прогресс парсинга"""

    if progress_mode == 'on' and out_path != 'stdout':
        print(f'{len(tasks)} items left')


def get_pipeline(out_path, out_format, progress_mode):
    """Factory функция для определения нужного пайплайна для обработки"""

    if out_format == 'mongodb':
        return MongoPipeline(out_path, out_format, progress_mode)
    elif out_format == 'csv':
        return CSVPipeline(out_path, out_format, progress_mode)
    elif out_format == 'jl':
        return JLPipeline(out_path, out_format, progress_mode)
