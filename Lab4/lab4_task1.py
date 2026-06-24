"""
Лабораторна робота №4 — Завдання 1
List/dict comprehension, any/all, генератори
"""

import random

# 1. List comprehension з 10 випадкових чисел
random_numbers = [random.randint(1, 100) for _ in range(10)]
print("10 випадкових чисел:", random_numbers)

# 2. Прізвища студентів, що здали предмет (оцінка >= 50)
grades = {
    "Іваненко": 85,
    "Петренко": 42,
    "Коваленко": 73,
    "Шевченко": 50,
    "Бондаренко": 38,
}
passed = [surname for surname, grade in grades.items() if grade >= 50]
print("Здали предмет:", passed)

# 3. Перевірка умови '0' <= i <= '9'
test_chars = ["5", "a", "0", "9", "z"]
for ch in test_chars:
    print(f"'{ch}': '0' <= i <= '9' -> {'0' <= ch <= '9'}")

# 4. Тільки цифри з текстового рядка (як int)
text = "grt743gfcg0r3"
digits = [int(i) for i in text if "0" <= i <= "9"]
print(f"Цифри з '{text}':", digits)  # [7, 4, 3, 0, 3]

# 5. Dict comprehension: ключ — елемент списку, значення — остача від ділення на 10
numbers = [45, 67, 24, 45]
remainder_dict = {n: n % 10 for n in numbers}
print("Словник остач:", remainder_dict)  # {45: 5, 67: 7, 24: 4}

# 6. any() та all() через генератор
data = [12, 45, 78, 120, 95]
has_over_100 = any(x > 100 for x in data)
all_over_100 = all(x > 100 for x in data)
print(f"Є число > 100: {has_over_100}")   # True
print(f"Усі числа > 100: {all_over_100}")  # False

# 7. Вираз-генератор (не list comprehension)
gen = (i**2 for i in range(5))
print("Генератор квадратів:", list(gen))  # [0, 1, 4, 9, 16]

# 8. Усні відповіді (без запуску на виведення)
print("\n--- Усні відповіді A0–A7 ---")
A0 = dict(zip(("a", "b", "c", "d", "e"), (1, 2, 3, 4, 5)))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
A4 = [i for i in A1 if i in A3]
A5 = {i: i * i for i in A1}
A6 = [[i, i * i] for i in A1]
A7 = [i if i % 2 else 0 for i in A1 if 2 < i < 8]

print("A0 =", A0)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print("A1 =", list(A1))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("A2 =", A2)  # [] — числа не є ключами словника A0
print("A3 =", A3)  # [1, 2, 3, 4, 5]
print("A4 =", A4)  # [1, 2, 3, 4, 5]
print("A5 =", A5)  # {0:0, 1:1, 2:4, ..., 9:81}
print("A6 =", A6)  # [[0,0], [1,1], ..., [9,81]]
print("A7 =", A7)  # [3, 0, 5, 0, 7]
