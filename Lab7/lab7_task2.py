"""
Лабораторна робота №7 — Завдання 2
Обчислювальні атрибути (@property): Circle та Triangle.
"""

import math


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def area(self) -> float:
        return math.pi * self.radius**2

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Сторони не утворюють трикутник")
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimeter(self) -> float:
        return self.a + self.b + self.c

    @property
    def area(self) -> float:
        s = self.perimeter / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


if __name__ == "__main__":
    circle = Circle(5)
    print("Circle:")
    print("  __dict__:", circle.__dict__)
    print("  radius:", circle.radius)
    print("  area:", round(circle.area, 4))
    print("  perimeter:", round(circle.perimeter, 4))

    triangle = Triangle(3, 4, 5)
    print("\nTriangle (3, 4, 5):")
    print("  __dict__:", triangle.__dict__)
    print("  perimeter:", triangle.perimeter)
    print("  area:", triangle.area)
