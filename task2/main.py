from typing import Generator, Callable


def generator_numbers(text: str) -> Generator[int, None, None]:
    words = text.split()
    for word in words:
        try:
            yield float(word)
        except ValueError:
            continue


def sum_profit(text: str, func: Callable[[str], Generator[int, None, None]]):
    return sum(func(text))


def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == '__main__':
    main()
