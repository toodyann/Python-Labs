"""
Лабораторна робота №3 — Завдання 1
Рядки: підрахунок слів та речень.
"""


def count_words(text: str) -> int:
    """Кількість слів (розділених пропусками)."""
    return len(text.split())


def count_sentences(text: str) -> int:
    """Кількість речень (завершуються . ? !)."""
    count = 0
    for char in text:
        if char in ".?!":
            count += 1
    return count


if __name__ == "__main__":
    text_words = "Python — це мова програмування високого рівня"
    text_sentences = "Привіт! Як справи? Все добре."

    print("=== Завдання 1: слова ===")
    print(f"Текст: {text_words!r}")
    print(f"Кількість слів: {count_words(text_words)}")

    print("\n=== Завдання 2: речення ===")
    print(f"Текст: {text_sentences!r}")
    print(f"Кількість речень: {count_sentences(text_sentences)}")

    print("\n--- Інтерактивно ---")
    user_text = input("Введіть текст: ")
    print(f"Слів: {count_words(user_text)}")
    print(f"Речень: {count_sentences(user_text)}")
