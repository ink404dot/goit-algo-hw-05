from typing import List, Dict
from sys import argv
from pathlib import Path
from collections import Counter


def load_logs(file_path: str) -> List:
    with open(file_path, encoding='UTF-8') as f:
        return [line.strip() for line in f.readlines()]


def parse_log_line(line: str) -> Dict[str, str]:
    return {key: value for key, value in zip(['date', 'time', 'level', 'message'],
                                             line.split(maxsplit=3))}


def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return list(filter(lambda log: log.get('level') == level, logs))
    


def count_logs_by_level(logs: list) -> dict:
    return dict(Counter([log.get('level') for log in logs]))


def display_log_counts(counts: dict):
    # Заголовок таблиці
    print(f"{'Level':<10} | {'Count':<10}")
    print("-" * 20)

    # Виводимо дані
    for level, count in counts.items():
        print(f"{level:<10} | {count:<10}")


def main():
    level_list = ('info', 'error', 'debug', 'warning')
    filtered_data = None
    if len(argv) > 1:
        path = Path(argv[1])
        if path.exists():
            log_data = []
            loaded_logs = load_logs(path)
            if loaded_logs:
                for line in load_logs(path):
                    log_data.append(parse_log_line(line))
                display_log_counts(count_logs_by_level(log_data))
                if len(argv) > 2 and argv[2].lower() in level_list:
                    level = argv[2].upper()
                    filtered_data = filter_logs_by_level(log_data, level)
                    print()
                    if filtered_data:
                        print(f'Деталі логів для рівня {level}:')
                        for log in filtered_data:
                            print(f"{log['date']} {log['time']} {log['level']} {log['message']}")
                    else:
                        print('Немає логів для рівня {level}')
            else:
                print('Немає даних в файлі')
        else:
            print('Файл не існує або не правильний шлях до файлу')
    else:
        print('Не введено шлях до файлу логів, як другий аргумент')
    


if __name__ == '__main__':
    main()
