"""
Лабораторна робота №6 — Завдання 1
Клас Student: оцінки за предметами, середні бали, залік.
"""


class Student:
    def __init__(self, surname: str, name: str, bal: dict[str, list] | None = None):
        self.surname = surname
        self.name = name
        self.bal = bal or {}

    def __str__(self) -> str:
        return f"{self.surname} {self.name}"

    def subjects(self) -> list[str]:
        """Предмети, які вивчає студент."""
        return list(self.bal.keys())

    def grades_for(self, subject: str) -> list:
        """Список оцінок за вказаний предмет."""
        return self.bal.get(subject, [])

    def avg_for(self, subject: str) -> float:
        """Середній бал за певний предмет."""
        grades = self.grades_for(subject)
        if not grades:
            return 0.0
        return sum(grades) / len(grades)

    def avg_all(self) -> float:
        """Середній бал за всі предмети."""
        all_grades = [grade for grades in self.bal.values() for grade in grades]
        if not all_grades:
            return 0.0
        return sum(all_grades) / len(all_grades)

    def passed(self, subject: str) -> bool:
        """Чи отримав залік за предмет (середній бал > 4)."""
        return self.avg_for(subject) > 4

    def add_subject(self, subject: str, grades: list) -> None:
        """Додати новий предмет з оцінками."""
        self.bal[subject] = list(grades)

    def add_grade(self, subject: str, grade) -> None:
        """Додати оцінку до існуючого предмету."""
        if subject not in self.bal:
            self.bal[subject] = []
        self.bal[subject].append(grade)

    def avg_by_subject(self) -> list[tuple[str, float]]:
        """Список пар (предмет, середній бал)."""
        return [(subject, self.avg_for(subject)) for subject in self.subjects()]

    def print_averages(self) -> None:
        """Вивести прізвище та середні бали по предметах."""
        print(self.surname, end="")
        for subject, average in self.avg_by_subject():
            print(f", {subject}: {average:.2f}", end="")
        print()


if __name__ == "__main__":
    stud = Student(
        "Іваненко",
        "Петро",
        {
            "Математика": [5, 4, 5],
            "Фізика": [3, 4, 4],
            "Python": [5, 5, 5],
        },
    )

    print(stud)
    print("Предмети:", stud.subjects())
    print("Оцінки з Python:", stud.grades_for("Python"))
    print("Сер. бал з Математики:", stud.avg_for("Математика"))
    print("Сер. бал за всі предмети:", round(stud.avg_all(), 2))
    print("Залік з Python:", stud.passed("Python"))
    print("Залік з Фізики:", stud.passed("Фізика"))

    stud.add_subject("Англійська", [4, 5])
    stud.add_grade("Фізика", 5)
    stud.print_averages()

    print("\n--- Примітки з завдання ---")
    print("isinstance(stud, Student):", isinstance(stud, Student))
    print("type(stud):", type(stud))
    print("stud.__dict__:", stud.__dict__)
