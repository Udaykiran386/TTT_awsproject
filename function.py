from typing import Union


def calc_on_numbers(a: Union[int, float], b: int) -> Union[int, float]:
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")

    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Division by zero is not allowed.")

    return a ** b


if __name__ == "__main__":
    calc_on_numbers(10, 5)
    calc_on_numbers(20.6, 5.2)
