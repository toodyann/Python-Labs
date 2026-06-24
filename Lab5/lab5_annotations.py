"""
Лабораторна робота №5 — анотації типів (підготовка до захисту).
"""

import random
from collections.abc import Iterator
from typing import Any


def task(b: str) -> dict[str, int]:
    return {i: b.count(i) for i in b.split()}


def task2(surnames: tuple[str, ...]) -> dict[int, str]:
    rnd_mark = tuple(random.sample(range(1, 100), 5))
    stud = {rnd_mark[i]: surnames[i] for i in range(len(rnd_mark))}
    return stud


def task3(cols: int, rows: int) -> list[list[int]]:
    a = [[1 if not (i + j) % 2 else 0 for j in range(cols)] for i in range(rows)]
    return a


def task_unique(a: list[Any]) -> bool:
    return len(a) == len(set(a))


def task4(data: tuple[int, int]) -> tuple[int, int]:
    x, y = data
    return x * 2, y * 2


def gen_binary() -> Iterator[str]:
    while True:
        for x in range(2):
            for y in range(2):
                yield str(x) + str(y)


if __name__ == "__main__":
    surnames = ("kolobok", "did", "baba", "zayec", "vovk")
    print("task2:", task2(surnames))

    my_gen = gen_binary()
    print("gen_binary:", [next(my_gen) for _ in range(4)])
