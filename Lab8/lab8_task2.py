"""
Лабораторна робота №8 — Завдання 2
Клас-ітератор для чисел з проміжку (початок, кінець, крок).
"""


class Iteration:
    """Приклад з методички: числа від 1 до end включно."""

    def __init__(self, end: int):
        self.number = 0
        self.end = end

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.number >= self.end:
            raise StopIteration
        self.number += 1
        return self.number


class RangeStepIterator:
    """Ітератор для проміжку [start, end] з заданим кроком."""

    def __init__(self, start: int, end: int, step: int = 1):
        if step == 0:
            raise ValueError("Крок не може бути нулем")
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.step > 0 and self.current > self.end:
            raise StopIteration
        if self.step < 0 and self.current < self.end:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value


if __name__ == "__main__":
    print("=== Iteration(7) з методички ===")
    print(list(Iteration(7)))

    print("\n=== RangeStepIterator(2, 10, 2) ===")
    print(list(RangeStepIterator(2, 10, 2)))

    print("\n=== RangeStepIterator(10, 0, -3) ===")
    print(list(RangeStepIterator(10, 0, -3)))

    print("\n=== for i in Iteration(5) ===")
    for i in Iteration(5):
        print(i, end=" ")
    print()
