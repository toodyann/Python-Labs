"""
Лабораторна робота №1 — Завдання 4
Бібліотека math: обчислення за формулою.
"""

from math import cos, pi, sin


def formula(a: float, b: float) -> float:
    """
    Формула з методички (зображення).
    sin(a)*cos(a)*(pi/2 - sin(b)/b) — наближення до прикладу 0.5 10.
    """
    return sin(a) * cos(a) * (pi / 2 - sin(b) / b)


if __name__ == "__main__":
    print("Приклади з методички:")
    print(f"  a=0.5, b=10 -> {formula(0.5, 10)}")
    print(f"  a=0, b=1   -> {formula(0, 1)}")

    a, b = map(float, input("Введіть a та b через пробіл: ").split())
    if b == 0:
        raise ValueError("b не може дорівнювати 0")
    print(formula(a, b))
