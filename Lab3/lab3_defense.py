"""
Лабораторна робота №3 — підготовка до захисту
Перетворення типів, розпакування, приклади структур даних.
"""

# --- Перетворення типів (з методички) ---

a_words = ["good", "better", "the best"]
b_nums = [4, 0, 4]

c_set = {"Сидоренко", "Петрів", "Дорош"}
grades = {"Denys": 45, "Olek": 89, "Ivan": 100}
text = "all right"


def type_conversions() -> None:
    print("=== Списки -> інші типи ===")
    print("tuple(a):", tuple(a_words))
    print("set(a):", set(a_words))
    print("dict(zip):", dict(zip(a_words, b_nums)))
    print("join str:", "".join(map(str, b_nums)))
    print("об'єднання:", a_words + list(map(str, b_nums)))

    print("\n=== Множина -> інші типи ===")
    print("list(c):", list(c_set))
    print("tuple(c):", tuple(c_set))
    print("fromkeys:", dict.fromkeys(c_set, 100))
    print("об'єднання:", c_set | {"Вітенко", "Дорош"})

    print("\n=== Словник -> інші типи ===")
    print("keys list:", list(grades.keys()))
    print("values tuple:", tuple(grades.values()))
    print("keys join:", " ".join(grades.keys()))
    print("merged:", {**grades, **{"Сидоренко": 34}})

    print("\n=== Рядок -> інші типи ===")
    print("list chars:", list(text))
    print("split words:", text.split())
    print("fromkeys words:", dict.fromkeys(text.split()))


def unpacking_demo() -> None:
    print("\n=== Розпакування ===")
    a, b, c = [1, 2, 3]
    print(f"a, b, c = [1,2,3] -> {a}, {b}, {c}")

    a, b, c = (0, 1, (2, 3, 4))
    print(f"a, b, c = (0,1,(2,3,4)) -> {a}, {b}, {c}")

    a, *b = [1, 2, 3]
    print(f"a, *b = [1,2,3] -> {a}, {b}")

    a, *b, c = [1, 2, 3, 4, 5]
    print(f"a, *b, c = [1,2,3,4,5] -> {a}, {b}, {c}")

    print("*a, b, *c = [1,2,3,4,5] -> SyntaxError (два * у присвоєнні)")

    a, _, b = [1, 2, 3]
    print(f"a, _, b = [1,2,3] -> {a}, _, {b}")


# --- Приклади вкладених структур (lab3-a) ---

drinks = {
    "martini": {"vodka", "vermouth"},
    "black man": {"vodka", "kahlua"},
    "white man": {"cream", "kahlua", "vodka"},
}

pets = [
    {"name": "Buddy", "species": "Dog", "owner": {"name": "Alice", "phone": "123-456"}},
    {"name": "Mittens", "species": "Cat", "owner": {"name": "Bob", "phone": "789-012"}},
]


if __name__ == "__main__":
    type_conversions()
    unpacking_demo()

    print("\n=== Приклад: drinks (dict) ===")
    print(f"martini: {drinks['martini']}")

    print("\n=== Приклад: pets (list of dicts) ===")
    for pet in pets:
        print(f"{pet['name']} ({pet['species']}) — власник {pet['owner']['name']}")
