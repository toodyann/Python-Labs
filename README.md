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
├── Lab4/
├── Lab5/
├── Lab6/
├── Lab7/
└── Lab8/
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
