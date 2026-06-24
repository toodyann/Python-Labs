"""
Лабораторна робота №5 — обробка балів з CSV-файлу.
Генератор для зчитування рядків, підрахунок сум, запис у текстовий файл.
"""

from pathlib import Path

CSV_FILE = Path(__file__).parent / "KN-2.csv"
OUTPUT_FILE = Path(__file__).parent / "results.txt"


def iter_lines(path: Path):
    """Генератор-вираз для зчитування рядків з файлу."""
    with path.open(encoding="utf-8") as file:
        lines = (line.strip() for line in file)
        yield from lines


def lab_points(value: str) -> int:
    """'+' за лабораторну = 2 бали."""
    return 2 if value.strip() == "+" else 0


def lab3_points(value: str) -> int:
    """'5/6' -> 5 + 6 балів."""
    earned, maximum = value.split("/")
    return int(earned) + int(maximum)


def test_points(value: str) -> int:
    """Переведення зі 100-бальної системи в 20-бальну."""
    return int(value) // 5


def student_total(row: str) -> tuple[str, int]:
    """Підрахунок суми балів для одного студента."""
    student, lab1, lab2, lab3, test, kr1 = row.split(",")
    total = (
        lab_points(lab1)
        + lab_points(lab2)
        + lab3_points(lab3)
        + test_points(test)
        + int(kr1)
    )
    return student, total


def process_grades(csv_path: Path, output_path: Path) -> list[tuple[str, int]]:
    lines = iter_lines(csv_path)
    next(lines)  # пропустити заголовок
    results = [student_total(line) for line in lines if line]

    with output_path.open("w", encoding="utf-8") as file:
        for student, total in results:
            file.write(f"{student}: {total}\n")

    return results


if __name__ == "__main__":
    scores = process_grades(CSV_FILE, OUTPUT_FILE)
    print("Сума балів по студентах:")
    for name, total in scores:
        print(f"  {name}: {total}")
    print(f"\nРезультати записано у {OUTPUT_FILE.name}")
