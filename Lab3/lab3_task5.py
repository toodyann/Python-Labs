"""
Лабораторна робота №3 — Завдання 5
Група студентів: середні бали, словник, список прізвищ.
"""

group = [
    {"surname": "Liv", "name": "Maria", "marks": [5, 5, 4]},
    {"surname": "Dobrov", "name": "Olek", "marks": [3, 1, 3, 2]},
    {"surname": "Koval", "name": "Iryna", "marks": [5, 4, 5, 5]},
    {"surname": "Melnyk", "name": "Andrii", "marks": [4, 4, 3, 5]},
    {"surname": "Bondar", "name": "Oksana", "marks": [5, 5, 5, 4, 5]},
]


def average(marks: list) -> float:
    return sum(marks) / len(marks)


if __name__ == "__main__":
    print("=== 1. Перший студент ===")
    print(group[0])

    print("\n=== 2. Дані групи ===")
    for person in group:
        print(
            person["surname"].ljust(10),
            person["name"].ljust(8),
            person["marks"],
        )

    print("\n=== 3. Середній бал кожного ===")
    for person in group:
        avg = average(person["marks"])
        print(f"{person['surname']}: {avg:.2f}")

    print("\n=== 4. Словник: прізвище -> середній бал ===")
    avg_dict = {person["surname"]: average(person["marks"]) for person in group}
    print(avg_dict)

    print("\n=== 5. Список прізвищ ===")
    surnames = [person["surname"] for person in group]
    print(surnames)
