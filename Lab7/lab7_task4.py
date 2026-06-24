"""
Лабораторна робота №7 — Завдання 4
Спеціальні (магічні) методи: __call__, __abs__, колекції, оператори, ітератори, генератори.
"""

import math


# --- Спеціальні поля класу та екземпляра ---


class Pet:
    def __init__(self, name: str):
        self._name = name


class Cat(Pet):
    def voice(self) -> str:
        return f"{self._name} says Meow"


def demo_special_fields() -> None:
    print("=== Спеціальні поля ===")
    print("Ім'я класу (__name__):", Cat.__name__)
    print("Базовий клас (__bases__):", Cat.__bases__)
    cat = Cat("Tom")
    print("Атрибути екземпляру (__dict__):", cat.__dict__)


# --- __call__ ---


class Polynom:
    """Поліном як словник {степінь: коефіцієнт}."""

    def __init__(self):
        self._coeffs: dict[int, float] = {}

    def set(self, power: int, coef: float) -> None:
        self._coeffs[power] = coef

    def __call__(self, x: float) -> float:
        return sum(a * x**i for i, a in self._coeffs.items())


# --- __abs__, перевантаження операторів ---


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x:.4f}, {self.y:.4f})"

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector2D") -> float:
        return self.x * other.x + self.y * other.y

    def __abs__(self) -> float:
        return (self * self) ** 0.5

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __iadd__(self, other: "Vector2D") -> "Vector2D":
        self.x += other.x
        self.y += other.y
        return self

    def __neg__(self) -> "Vector2D":
        return Vector2D(-self.x, -self.y)


class RectTriangle:
    """Прямокутний трикутник."""

    def __init__(self, a: float, b: float):
        self._a = a
        self._b = b

    def __str__(self) -> str:
        return f"Прямокутний трикутник з катетами {self._a:.4f} та {self._b:.4f}"


# --- Методи для колекцій ---


class Collection:
    """Захищений список зі спеціальними методами колекції."""

    def __init__(self):
        self.__elements: list = []

    def __setitem__(self, key: int, value) -> None:
        try:
            self.__elements[key] = value
        except IndexError:
            self.__elements.append(value)

    def __getitem__(self, key: int):
        try:
            return self.__elements[key]
        except IndexError:
            return None

    def __contains__(self, item) -> bool:
        return item in self.__elements

    def __delitem__(self, key: int) -> None:
        try:
            self.__elements.pop(key)
        except IndexError:
            pass

    def __len__(self) -> int:
        return len(self.__elements)

    def __str__(self) -> str:
        return str(self.__elements)


# --- Ітератор та ітерований об'єкт ---


class ListIterator:
    def __init__(self, collection: list):
        self._collection = collection
        self._cursor = 0

    def __next__(self):
        try:
            value = self._collection[self._cursor]
            self._cursor += 1
            return value
        except IndexError:
            raise StopIteration from None


class Iterable:
    def __init__(self):
        self.__container: list = []

    def append(self, value) -> None:
        self.__container.append(value)

    def __getitem__(self, item: int):
        return self.__container[item]

    def __iter__(self):
        return ListIterator(self.__container)


# --- Генератор (клас) ---


class FactorialGenerator:
    """Генератор факторіалів: 1, 1, 2, 6, 24, ..."""

    def __init__(self, n: int):
        self._n = n
        self._k = 0
        self._f = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._k == 0:
            self._k = 1
            return 1
        if self._k <= self._n:
            self._f *= self._k
            self._k += 1
            return self._f
        raise StopIteration


# --- Функції-генератори ---


def factorial_generator(n: int):
    yield 1
    f = 1
    for k in range(1, n + 1):
        f *= k
        yield f


def fibonacci():
    f2 = f1 = 1
    yield f2
    yield f1
    while True:
        f2, f1 = f1, f1 + f2
        yield f1


if __name__ == "__main__":
    demo_special_fields()

    print("\n=== __call__ (Polynom) ===")
    p = Polynom()
    p.set(0, 1)
    p.set(1, 2)
    p.set(2, 1)
    x = 2.0
    print(f"P({x}) = {p(x)}")

    print("\n=== Vector2D ===")
    v1 = Vector2D(1, 3)
    v2 = Vector2D(4, 2)
    print("v1 + v2:", v1 + v2)
    print("v1 - v2:", v1 - v2)
    print("v1 * v2:", v1 * v2)
    print("abs(Vector2D(3, 4)):", abs(Vector2D(3, 4)))
    print("v1 == v2:", v1 == v2)
    v2 += v1
    print("v2 += v1:", v2)
    print("-Vector2D(3, 4):", -Vector2D(3, 4))

    print("\n=== __str__ (RectTriangle) ===")
    print(RectTriangle(3, 4))

    print("\n=== Collection ===")
    c = Collection()
    c[0] = 0
    c[1] = 1
    c[5] = 5
    c[2] = 2
    print("Колекція:", c)
    print("c[1]:", c[1])
    print("2 in c:", 2 in c)
    print("len(c):", len(c))
    del c[0]
    print("після del c[0]:", c)

    print("\n=== Iterable / Iterator ===")
    items = Iterable()
    for value in (1, 2, 3, 4):
        items.append(value)
    print("for x in items:", [x for x in items])

    print("\n=== FactorialGenerator (клас) ===")
    print(list(FactorialGenerator(5)))

    print("\n=== factorial_generator (yield) ===")
    print(list(factorial_generator(5)))

    print("\n=== fibonacci (перші 8) ===")
    gen = fibonacci()
    print([next(gen) for _ in range(8)])
