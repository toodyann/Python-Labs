"""Модуль для обчислення параметрів кола за радіусом."""

from math import pi

__all__ = ["diameter", "circumference", "area"]


def diameter(r: float) -> float:
    """Діаметр кола."""
    return 2 * r


def circumference(r: float) -> float:
    """Довжина кола."""
    return 2 * pi * r


def area(r: float) -> float:
    """Площа кола."""
    return pi * r**2
