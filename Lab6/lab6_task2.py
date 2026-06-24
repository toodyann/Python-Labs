"""
Лабораторна робота №6 — Завдання 2
Клас Vector: перевантаження операторів.
"""

import math


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other: "Vector") -> float:
        """Скалярний добуток двох векторів."""
        return self.x * other.x + self.y * other.y

    def __len__(self) -> int:
        return int(math.hypot(self.x, self.y))

    def length(self) -> float:
        """Точна довжина вектора."""
        return math.hypot(self.x, self.y)

    def is_perpendicular(self, other: "Vector") -> bool:
        """Чи перпендикулярні вектори (скалярний добуток = 0)."""
        return self * other == 0


if __name__ == "__main__":
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    v3 = Vector(3, 4)
    v4 = Vector(-4, 3)

    print("v1:", v1)
    print("v2:", v2)
    print("v1 == v3:", v1 == v3)
    print("v1 == v2:", v1 == v2)
    print("v1 + v2:", v1 + v2)
    print("v1 * v2 (скалярний):", v1 * v2)
    print("len(v1):", len(v1))
    print("length(v1):", v1.length())
    print("v1 ⊥ v4:", v1.is_perpendicular(v4))
