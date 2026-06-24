"""
Лабораторна робота №4 — Завдання 2
Введення, перетворення, сума, розпакування
"""

# 1. Введення чисел через пробіл
raw = input("Введіть числа через пробіл: ")
numbers = raw.split()

# 2. Перетворення в int
numbers = [int(x) for x in numbers]

# 3. Сума елементів
total = sum(numbers)
print("Список:", numbers)
print("Сума:", total)

# 4. Розпакування
if len(numbers) == 3:
    x, y, z = numbers
    print(f"Розпакування (3 числа): x={x}, y={y}, z={z}")
elif len(numbers) > 3:
    x, *y, z = numbers
    print(f"Розпакування (більше 3): x={x}, y={y}, z={z}")
else:
    print("Для розпакування потрібно щонайменше 3 числа.")
