"""
Лабораторна робота №1 — Завдання 5
Сума 1 + x + x^2 + ... + x^n без готової формули.
"""


def geom_sum(n: int, x: float) -> float:
    total = 0.0
    power = 1.0
    for _ in range(n + 1):
        total += power
        power *= x
    return total


if __name__ == "__main__":
    n, x = input("Введіть n та x через пробіл: ").split()
    n = int(n)
    x = float(x)
    print(geom_sum(n, x))

    print("\nПриклад: n=4, x=0.1 ->", geom_sum(4, 0.1))
