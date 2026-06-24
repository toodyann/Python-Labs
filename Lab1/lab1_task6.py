"""
Лабораторна робота №1 — Завдання 6
Відгадування числа методом поділу навпіл (0–100).
"""


def guess_number() -> None:
    low, high = 0, 100

    while True:
        guess = (low + high) // 2
        print(f"Ви загадали число {guess}?")
        answer = input("Так / більше / менше: ").strip().lower()

        if answer in ("так", "yes", "y", "т"):
            print(f"Загадане число: {guess}")
            break
        if answer in ("більше", "б", ">"):
            low = guess
        elif answer in ("менше", "м", "<"):
            high = guess
        else:
            print("Введіть: так / більше / менше")


if __name__ == "__main__":
    print("Загадайте число від 0 до 100")
    guess_number()
