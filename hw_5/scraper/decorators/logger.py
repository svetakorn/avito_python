import time
import datetime
import os

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
