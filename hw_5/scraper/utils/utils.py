import datetime


def get_current_time_formatted(format_str: str) -> str:
    return datetime.datetime.now().strftime(format_str)
