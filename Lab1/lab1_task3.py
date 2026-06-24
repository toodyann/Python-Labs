"""
Лабораторна робота №1 — Завдання 3
Розгалуження: правильні закінчення для слова «студент».
"""


def student_word(n: int) -> str:
    """Повертає 'студент', 'студенти' або 'студентів'."""
    if n % 100 in (11, 12, 13, 14):
        return "студентів"
    if n % 10 == 1:
        return "студент"
    if n % 10 in (2, 3, 4):
        return "студенти"
    return "студентів"


def zalik_phrase(n: int) -> str:
    return f"Залік здали... {n} {student_word(n)}"


if __name__ == "__main__":
    n = int(input("Введіть натуральне число n (< 100): "))
    if not 0 < n < 100:
        raise ValueError("n має бути натуральним числом менше 100")
    print(zalik_phrase(n))

    print("\nПриклади:")
    for value in (1, 2, 5, 11, 21, 22, 25):
        print(f"  n={value}: {zalik_phrase(value)}")

    print("\nmatch-case працює з Python 3.10+")
