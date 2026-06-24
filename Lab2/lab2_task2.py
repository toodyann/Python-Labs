"""
Лабораторна робота №2 — Завдання 2
Обробка винятків: обчислення 1/x.
"""


def reciprocal() -> None:
    try:
        x = int(input("Введіть натуральне число x: "))
        print(1 / x)
    except ZeroDivisionError:
        print("Ділити на нуль не можна")
    except ValueError:
        print("text!!!")


if __name__ == "__main__":
    reciprocal()
