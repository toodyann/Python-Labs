"""
Лабораторна робота №8 — Завдання 1
Декоратори.
"""

from random import randint


# --- Базові приклади з методички ---


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("функція-обгортка починається")
        result = func(*args, **kwargs)
        print("функція-обгортка закінчується")
        return result

    return wrapper


@my_decorator
def simple_function():
    print("а це наша функція")


@my_decorator
def simple_function_with_arg(z):
    print("а це наша функція")


def dec_1(example_1):
    def wrapper():
        return "".join(map(str, example_1()))

    return wrapper


@dec_1
def example_1():
    return list(range(5))


def dec_2(example_2):
    def wrapper(z):
        return "".join(map(str, example_2(z)))

    return wrapper


@dec_2
def example_2(z):
    return [randint(1, 9) for _ in range(z)]


def dec_3(example_3):
    def wrapper(z):
        if isinstance(z, int):
            return example_3(z)
        return "Потрібно натуральне число"

    return wrapper


@dec_3
def example_3(z):
    return [randint(1, 9) for _ in range(z)]


# --- 1.1 makebold / makeitalic ---


def makebold(func):
    def wrapper():
        return f"<b>{func()}</b>"

    return wrapper


def makeitalic(func):
    def wrapper():
        return f"<i>{func()}</i>"

    return wrapper


def get_text() -> str:
    return "Привіт, Python!"


@makebold
@makeitalic
def text_bold_then_italic():
    return get_text()


@makeitalic
@makebold
def text_italic_then_bold():
    return get_text()


# --- 1.2 Паліндром ---


def clean_text(func):
    def wrapper(text: str) -> str:
        cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
        return func(cleaned)

    return wrapper


@clean_text
def is_palindrome(text: str) -> bool:
    return text == text[::-1]


# --- 1.3 Обмін ключів і значень у словнику ---


def check_unique_values(func):
    def wrapper(data: dict):
        values = list(data.values())
        if len(values) != len(set(values)):
            return "Неможливо обміняти: є повторення серед значень"
        return func(data)

    return wrapper


@check_unique_values
def swap_keys_values(data: dict) -> dict:
    return {value: key for key, value in data.items()}


# --- 1.4 Унікальність елементів ---


def normalize_input(func):
    def wrapper(data):
        if isinstance(data, int):
            data = [int(d) for d in str(abs(data))]
        elif isinstance(data, str):
            data = list(data)
        elif not isinstance(data, (list, tuple, dict, set)):
            raise TypeError("Очікується list, tuple, dict, set, int або str")
        return func(data)

    return wrapper


@normalize_input
def all_unique(data) -> bool:
    if isinstance(data, dict):
        items = list(data.values())
    elif isinstance(data, set):
        items = list(data)
    else:
        items = list(data)
    return len(items) == len(set(items))


if __name__ == "__main__":
    print("=== Базові декоратори ===")
    simple_function()
    simple_function_with_arg("тест")
    print("example_1():", example_1())
    print("example_2(3):", example_2(3))
    print("example_3(3):", example_3(3))
    print("example_3('3'):", example_3("3"))

    print("\n=== 1.1 makebold / makeitalic ===")
    print("@makebold @makeitalic:", text_bold_then_italic())
    print("@makeitalic @makebold:", text_italic_then_bold())

    print("\n=== 1.2 Паліндром ===")
    phrase = "Я несу гусеня"
    print(f"'{phrase}' -> паліндром:", is_palindrome(phrase))
    print("'python' -> паліндром:", is_palindrome("python"))

    print("\n=== 1.3 swap_keys_values ===")
    ok = {"a": 1, "b": 2, "c": 3}
    bad = {"a": 1, "b": 1, "c": 2}
    print("ok:", swap_keys_values(ok))
    print("bad:", swap_keys_values(bad))

    print("\n=== 1.4 all_unique ===")
    print("[1, 2, 3]:", all_unique([1, 2, 3]))
    print("[1, 2, 2]:", all_unique([1, 2, 2]))
    print("1221 (число):", all_unique(1221))
    print("'aba' (рядок):", all_unique("aba"))
    print("{1, 2, 3}:", all_unique({1, 2, 3}))
