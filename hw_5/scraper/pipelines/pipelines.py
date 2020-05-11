import json
import csv
import sys
from pymongo import MongoClient
from scraper.decorators.decorators import timer
from typing import Dict, NoReturn


class AbstractPipeline:

    def __init__(self, out_path: str, out_format: str, progress_mode: str):
        self.out_path = out_path
        self.out_format = out_format
        self.progress_mode = progress_mode
        self.out_file = None

    def open_spider(self) -> NoReturn:
        """Метод класса для открытия файла/подключения к базе"""
        pass

    def close_spider(self) -> NoReturn:
        """Метод класса для закрытия файла/подключения"""
        pass

    def process_item(self, item) -> NoReturn:
        """Обрабатывает один объект парсинга"""
        pass


class CSVPipeline(AbstractPipeline):

    def __init__(self, out_path: str, out_format: str, progress_mode: str):
        super().__init__(out_path, out_format, progress_mode)
        self.writer = None

    @timer
    def open_spider(self):
        if self.out_path == 'stdout':
            self.out_file = sys.stdout
            return

        self.out_file = open(self.out_path + '.' + self.out_format, 'w', buffering=1)

    @timer
    def close_spider(self):
        self.out_file.close()

    @timer
    def process_item(self, item: Dict):
        if self.writer is None:
            self.writer = csv.DictWriter(self.out_file, fieldnames=item.keys())

        if self.out_file.tell() == 0:
            self.writer.writeheader()
        self.writer.writerow(item)


class JLPipeline(AbstractPipeline):

    def __init__(self, out_path: str, out_format: str, progress_mode: str):
        super().__init__(out_path, out_format, progress_mode)

    @timer
    def open_spider(self):
        if self.out_path == 'stdout':
            self.out_file = sys.stdout
            return

        self.out_file = open(self.out_path + '.' + self.out_format, 'w', buffering=1)

    @timer
    def close_spider(self):
        self.out_file.close()

    @timer
    def process_item(self, item: Dict):
        line = json.dumps(item) + '\n'
        self.out_file.write(line)


class MongoPipeline(AbstractPipeline):
    _dbc = 'mongodb://localhost:32769'

    def __init__(self, out_path: str, out_format: str, progress_mode: str):
        super().__init__(out_path, out_format, progress_mode)
        self.db = None

    @timer
    def open_spider(self):
        if (self.out_format == 'mongodb') & (self.db is None):
            client = MongoClient(self._dbc)
            self.db = client.scraper_db
            self.db.rus_ultimate_players.remove({})
            return

    @timer
    def process_item(self, item: Dict):
        self.db.rus_ultimate_players.insert_one(item)

