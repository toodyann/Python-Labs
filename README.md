<p align="center">
  <img src="assets/python-banner.svg?v=2" alt="PYTHON" width="480"/>
</p>

<h1 align="center">Python Labs</h1>

<p align="center">
  Репозиторій з лабораторними роботами з курсу <strong>Python</strong> (КНУ)
</p>

## Вимоги

- Python 3.10+
- Залежності потрібні лише для **Lab4** (`requests`)

```bash
cd Lab4
pip install -r requirements.txt
```

## Запуск

Кожна лабораторна — окрема папка. Усередині — файли з завданнями; більшість можна запускати напряму:

```bash
cd Lab5
python3 lab5_grades.py
```

## Структура

```
Python Labs/
├── Lab1/
├── Lab2/
├── Lab3/
├── Lab4/
├── Lab5/
├── Lab6/
├── Lab7/
└── Lab8/
```

---

## Lab1 — Типи даних, введення/виведення, цикли

| Файл | Тема |
|------|------|
| `lab1_task1.py` | усні відповіді: типи, кортежі, `type()` / `isinstance()` |
| `lab1_task2.py` | введення, перетворення типів, `print(sep, end)` |
| `lab1_task3.py` | розгалуження: «студент / студенти / студентів» |
| `lab1_task4.py` | бібліотека `math`, обчислення за формулою |
| `lab1_task5.py` | сума геометричної прогресії `1 + x + … + x^n` |
| `lab1_task6.py` | відгадування числа методом поділу навпіл |

```bash
cd Lab1
python3 lab1_task1.py
python3 lab1_task6.py
```

---

## Lab2 — Списки, копіювання, винятки, меню

| Файл | Тема |
|------|------|
| `lab2_task1.py` | списки, усні відповіді, shallow/deep copy |
| `lab2_task2.py` | `try/except`: обчислення `1/x` |
| `lab2_task3.py` | інтерактивне меню роботи зі списком |

```bash
cd Lab2
python3 lab2_task1.py
python3 lab2_task3.py
```

---

## Lab3 — Рядки, множини, словники, структури даних

| Файл | Тема |
|------|------|
| `lab3_task1.py` | підрахунок слів і речень у тексті |
| `lab3_task2.py` | множини: перетин, відсутні цифри, розділові знаки |
| `lab3_task3.py` | словник оцінок, середній бал, заборгованості |
| `lab3_task4.py` | магазин: купівля товарів до введення «ок» |
| `lab3_task5.py` | група студентів: середні бали, словник, прізвища |
| `lab3_defense.py` | перетворення типів, розпакування, вкладені структури |

```bash
cd Lab3
python3 lab3_task2.py
python3 lab3_task3.py
python3 lab3_task4.py
```

---

## Lab4 — Comprehension, введення, API

| Файл | Тема |
|------|------|
| `lab4_task1.py` | list/dict comprehension, `any`/`all`, генератори |
| `lab4_task2.py` | введення, перетворення типів, розпакування |
| `lab4_task3.py` | HTTP-запит до API курсів валют ПриватБанку |

```bash
cd Lab4
python3 lab4_task1.py
python3 lab4_task2.py
python3 lab4_task3.py
```

---

## Lab5 — Файли, генератори, лямбди, модулі

| Файл | Тема |
|------|------|
| `lab5_grades.py` | зчитування CSV (`KN-2.csv`), підрахунок балів, запис у `results.txt` |
| `lab5_defense.py` | лямбда-функції та однорядкові вирази |
| `lab5_annotations.py` | анотації типів |
| `radius.py` | модуль: діаметр, довжина та площа кола |
| `radius_demo.py` | демонстрація модуля `radius` |

```bash
cd Lab5
python3 lab5_grades.py
python3 radius_demo.py
```

---

## Lab6 — Класи, наслідування, оператори

| Файл | Тема |
|------|------|
| `lab6_task1.py` | клас `Student`: оцінки, середні бали, залік |
| `lab6_task2.py` | клас `Vector`: `__add__`, `__eq__`, `__mul__`, `__len__` |
| `lab6_task3.py` | наслідування, MRO, трикутники (Герон → рівнобедрений → рівносторонній) |

```bash
cd Lab6
python3 lab6_task1.py
python3 lab6_task2.py
python3 lab6_task3.py
```

---

## Lab7 — Методи класу, property, інкапсуляція, dunder-методи

| Файл | Тема |
|------|------|
| `lab7_task1.py` | `@classmethod`, `@staticmethod`, методи екземпляра |
| `lab7_task2.py` | обчислювальні атрибути (`@property`): `Circle`, `Triangle` |
| `lab7_task3.py` | інкапсуляція: getter / setter / deleter |
| `lab7_task4.py` | спеціальні методи: `__call__`, `__abs__`, колекції, ітератори, генератори |

```bash
cd Lab7
python3 lab7_task1.py
python3 lab7_task2.py
python3 lab7_task3.py
python3 lab7_task4.py
```

---

## Lab8 — Декоратори та ітератори

| Файл | Тема |
|------|------|
| `lab8_task1.py` | декоратори: HTML-теги, паліндром, словник, унікальність |
| `lab8_task2.py` | клас-ітератор для проміжку з кроком |

```bash
cd Lab8
python3 lab8_task1.py
python3 lab8_task2.py
```
