import json
import typing
from collections import deque
import requests
import csv


FORMAT_CSV = 'csv'
FORMAT_JL = 'jl'
FILENAME = 'rus_ultimate_players'


def start(start_url: str, callback: typing.Callable, out_path: str, out_format: str):
    start_task = (start_url, callback)
    tasks = deque([start_task])

    if out_path == FILENAME:
        out_file = open(out_path + '.' + out_format, 'w', buffering=1)
    else:
        out_file = open(out_path, 'w', buffering=1)

    try:
        while tasks:
            url, callback = tasks.popleft()
            print(url)
            resp = requests.get(url)

            for result in callback(resp):
                if isinstance(result, dict):
                    if out_format == FORMAT_CSV:
                        _write_csv(result, out_file)
                    elif out_format == FORMAT_JL:
                        _write_jl(result, out_file)
                else:
                    tasks.append(result)
    finally:
        out_file.close()


def _write_jl(row, out_file):
    json.dump(row, out_file)
    out_file.write('\n')


def _write_csv(row, out_file):
    writer = csv.DictWriter(out_file, fieldnames=row.keys())
    if out_file.tell() == 0:
        writer.writeheader()
    writer.writerow(row)

