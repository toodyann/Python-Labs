"""
Лабораторна робота №1 — Завдання 2
Введення, виведення, перетворення типів (завдання 3–7).
"""


def task3() -> None:
    y = input("Введіть y: ")
    print(y * 3)


def task4_7() -> None:
    x = int(input("Введіть число (наприклад '10'): "))
    print(x)
    print(type(x))

    x = x + 0.8
    x = int(x)
    print(x)
    print(type(x))

    u = 7
    print(x, u, sep=";", end=" done\n")


if __name__ == "__main__":
    print("=== Завдання 3 ===")
    task3()
    print("\n=== Завдання 4–7 ===")
    task4_7()
