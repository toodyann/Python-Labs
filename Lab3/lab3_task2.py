"""
Лабораторна робота №3 — Завдання 2
Множини: операції та усні завдання 3–5.
"""

PUNCTUATION = {".", ",", ";", ":", "!", "?", "-"}


def common_elements(a: list, b: list) -> set:
    """Числа, що зустрічаються в обох списках."""
    return set(a) & set(b)


def missing_digits(digits: list) -> set:
    """Цифри 0–9, яких немає у списку."""
    return set(range(10)) - set(digits)


def punctuation_in_text(text: str) -> set:
    """Які з розділових знаків зустрічаються в тексті."""
    return PUNCTUATION & set(text)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [4, 5, 6, 7, 8]
    print("=== Завдання 3: спільні елементи ===")
    print(f"A = {a}")
    print(f"B = {b}")
    print(f"A & B = {common_elements(a, b)}")

    digits = [1, 3, 3, 5, 7, 9, 9]
    print("\n=== Завдання 4: відсутні цифри ===")
    print(f"Список: {digits}")
    print(f"Відсутні: {sorted(missing_digits(digits))}")

    sample = "Привіт, світ! Як справи?-добре."
    print("\n=== Завдання 5: розділові знаки ===")
    print(f"Текст: {sample!r}")
    print(f"Зустрічаються: {sorted(punctuation_in_text(sample))}")

    print("\n=== Методи множин (з методички) ===")
    A = {1, 2, 3}
    B = {3, 4, 5}
    print(f"A | B  = {A | B}")
    print(f"A & B  = {A & B}")
    print(f"A - B  = {A - B}")
    print(f"A ^ B  = {A ^ B}")
