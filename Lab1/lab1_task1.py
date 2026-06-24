"""
Лабораторна робота №1 — Завдання 1
Типи даних, усні відповіді, перетворення типів.
"""


def oral_types_demo() -> None:
    """Код з методички — усно визначити результат."""
    print("=== Усні відповіді (код з методички) ===")
    x = 2 * 3**2
    print(f"2*3**2 = {x}")  # 18

    x = 5
    print(f"2 < x < 9 -> {2 < x < 9}")  # True
    print(f"x < True -> {x < True}")  # False (True == 1)
    print(f"[0,1,2,3] is range(4) -> {[0, 1, 2, 3] is range(4)}")  # False
    print(f"[0,1,2,3] == range(4) -> {[0, 1, 2, 3] == range(4)}")  # False
    print(f"2 in [0,1,2,3] -> {2 in [0, 1, 2, 3]}")  # True
    print(f"2 in range(4) -> {2 in range(4)}")  # True
    print(
        f"5 in range(4) or 1 not in () and 1 in [1] -> "
        f"{5 in range(4) or 1 not in () and 1 in [1]}"
    )  # True


def oral_tuple_question() -> None:
    """Які з варіантів є кортежами?"""
    print("\n=== Кортежі (з методички) ===")
    examples = {
        "()": (),
        "''": "",
        "{}": {},
        "{1}": {1},
        "{1,}": {1,},
        "(True)": (True),  # noqa: SIM212 — це не кортеж
        "(True,)": (True,),
    }
    for name, value in examples.items():
        print(f"{name:10} -> {type(value).__name__}")


def type_conversions() -> None:
    """Усні відповіді: перетворення типів."""
    print("\n=== Перетворення типів ===")
    print(f"int(12.4) -> {int(12.4)}")
    print(f"float(10) -> {float(10)}")
    print(f"complex(20) -> {complex(20)}")
    print(f"str(10) -> {repr(str(10))}")


def type_vs_isinstance() -> None:
    print("\n=== type() vs isinstance() ===")
    x = 5
    print(f"type(x) is int -> {type(x) is int}")
    print(f"isinstance(x, int) -> {isinstance(x, int)}")
    print("type() — точний тип об'єкта; isinstance() — чи належить до класу/нащадка")


if __name__ == "__main__":
    oral_types_demo()
    oral_tuple_question()
    type_conversions()
    type_vs_isinstance()
