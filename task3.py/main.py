from typing import List, Dict
from sys import argv
from pathlib import Path
from collections import defaultdict, Counter


def load_logs(file_path: str) -> List:
    with open(file_path, encoding='UTF-8') as f:
        return [line.strip() for line in f.readlines()]


def parse_log_line(line: str) -> Dict[str, str]:
    return {key: value for key, value in zip(['date', 'time', 'level', 'message'], line.split(maxsplit=3))}


def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return list(filter(lambda log: log.get('level') == level, logs))


def count_logs_by_level(logs: list) -> dict:
    return dict(Counter([log.get('level') for log in logs]))


def display_log_counts(counts: dict):
    # Заголовок таблицы
    print(f"{'Level':<10} | {'Count':<10}")
    print("-" * 20)

    # Выводим данные
    for level, count in counts.items():
        print(f"{level:<10} | {count:<10}")


def main():
    level_list = ('info', 'error', 'debug', 'warning')
    path = Path(argv[1])
    if len(argv) > 2 and argv[2].lower() in level_list:
        level = argv[2].lower()


if __name__ == '__main__':
    main()
