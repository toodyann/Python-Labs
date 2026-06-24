"""
Лабораторна робота №3 — Завдання 3
Словники: оцінки студентів, середній бал, заборгованості.
"""

PASS_GRADE = 4


def average(grades: list) -> float:
    if not grades:
        return 0.0
    return sum(grades) / len(grades)


def count_debts(grades: list) -> int:
    """Кількість оцінок нижче прохідного балу."""
    return sum(1 for grade in grades if grade < PASS_GRADE)


def print_zalik(zalik: dict) -> None:
    print("=== Оцінки студентів ===")
    for key, value in zalik.items():
        print(f"{key}: {value}")

    print("\n=== Середній бал ===")
    for student, grades in zalik.items():
        print(f"{student}: {average(grades):.2f}")

    print("\n=== Заборгованості ===")
    total_debts = 0
    for student, grades in zalik.items():
        debts = count_debts(grades)
        total_debts += debts
        print(f"{student}: {debts}")
    print(f"Всього заборгованостей: {total_debts}")


if __name__ == "__main__":
    zalik = {
        "Федик": [5, 3, 2, 5],
        "Борисюк": [4],
        "Денис": [2, 3, 1],
        "Іваненко": [5, 5, 4, 5],
        "Петренко": [3, 4, 2, 5, 3],
    }

    print_zalik(zalik)

    print("\n=== Об'єднання словників ===")
    a = {"a": 1, "b": 2}
    b = {"c": 3, "d": 4}
    c = {**a, **b}
    print(c)
