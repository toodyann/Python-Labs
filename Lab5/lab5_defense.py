"""
Лабораторна робота №5 — підготовка до захисту.
Лямбда-функції та однорядкові вирази.
"""

import string

# 1. Середнє арифметичне списку чисел
avg = lambda nums: sum(nums) / len(nums)

# 2. Перевірка парності числа
is_even = lambda n: n % 2 == 0

# 3. Сума цифр в числі (один рядок)
digit_sum = lambda n: sum(int(d) for d in str(abs(n)))

# 4. Чи всі елементи списку унікальні (один рядок)
all_unique = lambda lst: len(lst) == len(set(lst))

# 5. Викинути розділові знаки з тексту (один рядок)
remove_punct = lambda text: "".join(ch for ch in text if ch not in string.punctuation)

# 6. Чи всі символи другого рядка є в першому? (один рядок)
chars_in_first = lambda s1, s2: set(s2) <= set(s1)

# 7. Поміняти місцями ключі та значення словника (один рядок)
swap_kv = lambda d: {v: k for k, v in d.items()}


if __name__ == "__main__":
    numbers = [10, 20, 30, 40]
    print("avg:", avg(numbers))
    print("is_even(4):", is_even(4))
    print("digit_sum(123):", digit_sum(123))
    print("all_unique([1,2,3]):", all_unique([1, 2, 3]))
    print("remove_punct:", remove_punct("Hello, world!"))
    print("chars_in_first:", chars_in_first("abcdef", "ace"))
    print("swap_kv:", swap_kv({"a": 1, "b": 2}))
