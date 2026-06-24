"""
Лабораторна робота №2 — Завдання 1
Списки: усні відповіді, поверхневе та глибоке копіювання.
"""

import copy


def oral_answers() -> None:
    print("=== Усні відповіді про списки ===")
    print(f"len([1, 2, [3, 4], 5]) -> {len([1, 2, [3, 4], 5])}")
    print(f"[1, 2] + [3, 4] -> {[1, 2] + [3, 4]}")
    print("[1, 2] + (3, 4) -> TypeError")
    print(f"[1, 2] + [3, 4, {{1, 2}}] -> {[1, 2] + [3, 4, {1, 2}]}")
    print("[1, 2] + 3 -> TypeError")
    print(f"[1, 2] * 3 -> {[1, 2] * 3}")
    print(f"[1, 2] == [1, 2] -> {[1, 2] == [1, 2]}")
    print(f"[1, 2] == [1, 2, None] -> {[1, 2] == [1, 2, None]}")
    print(f"[1, 2] == (1, 2) -> {[1, 2] == (1, 2)}")
    print("list(567) -> TypeError")
    print(f"list('ok') -> {list('ok')}")
    print(f"list({{65, 17, 23, 46}}) -> {sorted(list({65, 17, 23, 46}))}")
    print(f"list({{'Petro': 17, 'Ivan': 46}}) -> {list({'Petro': 17, 'Ivan': 46})}")
    print(f"list(range(5)) -> {list(range(5))}")
    print("list(True) -> TypeError")


def reference_demo() -> None:
    print("\n=== Посилання на список ===")
    a = [1, 2]
    b = a
    b.append(3)
    print(f"A = {a}, B = {b}  # B змінює той самий список")


def shallow_copy_demo() -> None:
    print("\n=== Поверхнева копія ===")
    a = [1, 2]
    b = a.copy()
    b.append(3)
    print(f"A = {a}, B = {b}")

    a = [1, [2, 3], 4]
    b = a.copy()
    a.append(5)
    a[1].append(6)
    print(f"A = {a}")
    print(f"B = {b}  # вкладений список спільний")


def deep_copy_demo() -> None:
    print("\n=== Глибока копія ===")
    a = [1, [2, 3], 4]
    b = copy.deepcopy(a)
    a.append(5)
    a[1].append(6)
    print(f"A = {a}")
    print(f"B = {b}  # повністю незалежна копія")


if __name__ == "__main__":
    oral_answers()
    reference_demo()
    shallow_copy_demo()
    deep_copy_demo()

    print("\nПоверхнева копія — для простих списків.")
    print("Глибока копія — коли є вкладені змінювані об'єкти.")
