import json
import csv
import sys
from pymongo import MongoClient


class AbstractPipeline:

    def __init__(self, out_path, out_format, progress_mode):
        self.out_path = out_path
        self.out_format = out_format
        self.progress_mode = progress_mode
        self.out_file = None

    def open_spider(self):
        pass

    def close_spider(self):
        pass

    def process_item(self, item):
        pass


class CSVPipeline(AbstractPipeline):

    def __init__(self, out_path, out_format, progress_mode):
        super().__init__(out_path, out_format, progress_mode)
        self.writer = None

    def open_spider(self):
        if self.out_path == 'stdout':
            self.out_file = sys.stdout
            return

        self.out_file = open(self.out_path + '.' + self.out_format, 'w', buffering=1)

    def close_spider(self):
        self.out_file.close()

    def process_item(self, item):
        if self.writer is None:
            self.writer = csv.DictWriter(self.out_file, fieldnames=item.keys())

        if self.out_file.tell() == 0:
            self.writer.writeheader()
        self.writer.writerow(item)


class JLPipeline(AbstractPipeline):

    def __init__(self, out_path, out_format, progress_mode):
        super().__init__(out_path, out_format, progress_mode)

    def open_spider(self):
        if self.out_path == 'stdout':
            self.out_file = sys.stdout
            return

        self.out_file = open(self.out_path + '.' + self.out_format, 'w', buffering=1)

    def close_spider(self):
        self.out_file.close()

    def process_item(self, item):
        line = json.dumps(item) + '\n'
        self.out_file.write(line)


class MongoPipeline(AbstractPipeline):
    _dbc = 'mongodb://localhost:32769'

    def __init__(self, out_path, out_format, progress_mode):
        super().__init__(out_path, out_format, progress_mode)
        self.db = None

    def open_spider(self):
        if (self.out_format == 'mongodb') & (self.db is None):
            client = MongoClient(self._dbc)
            self.db = client.scraper_db
            self.db.rus_ultimate_players.remove({})
            return

    def process_item(self, item):
        self.db.rus_ultimate_players.insert_one(item)

# + stdout csv - записать csv в stdout
# + stdout jl - записать jl в stdout
# + stdout mongodb - не разрешено, mongodb - приоритетно
# + file csv - записать csv в файл
# + file jl - записать jl в файд
# + file mongodb - не разрешено, mongodb - приоритетно
