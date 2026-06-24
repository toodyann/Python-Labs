"""
Лабораторна робота №6 — Завдання 3
Наслідування, MRO, трикутники (Герон, рівнобедрений, рівносторонній).
"""

import math


class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return f"{self.name} makes a sound"


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says Meow"


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Сторони не утворюють трикутник")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """Площа за формулою Герона."""
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class IsoscelesTriangle(Triangle):
    def __init__(self, equal_side: float, base: float):
        super().__init__(equal_side, equal_side, base)
        self.equal_side = equal_side
        self.base = base

    def area(self) -> float:
        height = math.sqrt(self.equal_side**2 - (self.base / 2) ** 2)
        return self.base * height / 2


class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, side: float):
        super().__init__(side, side)
        self.side = side

    def area(self) -> float:
        return (math.sqrt(3) / 4) * self.side**2


def print_mro_examples() -> None:
    """Приклади MRO з методички."""

    class A:
        pass

    class B:
        pass

    class A1(A):
        pass

    class B1(B):
        pass

    class C(A1, B1):
        pass

    print("C.mro():", [cls.__name__ for cls in C.mro()])

    class A2(A):
        pass

    class A3(A):
        pass

    class C2(A1, A2, A3):
        pass

    print("C2.mro():", [cls.__name__ for cls in C2.mro()])

    class B2(B):
        pass

    class C3(B1, B2):
        pass

    class D(A1, C3):
        pass

    print("D.mro():", [cls.__name__ for cls in D.mro()])


if __name__ == "__main__":
    animal = Animal("Generic Animal")
    cat = Cat("Whiskers")
    print(animal.speak())
    print(cat.speak())

    print()
    print_mro_examples()

    print()
    t = Triangle(3, 4, 5)
    iso = IsoscelesTriangle(5, 6)
    equ = EquilateralTriangle(4)

    print(f"Звичайний трикутник (3, 4, 5): площа = {t.area():.4f}")
    print(f"Рівнобедрений (5, 5, 6): площа = {iso.area():.4f}")
    print(f"Рівносторонній (4): площа = {equ.area():.4f}")
