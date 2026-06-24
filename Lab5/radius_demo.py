"""Перевірка функцій модуля radius."""

from radius import area, circumference, diameter

if __name__ == "__main__":
    r = 5.0
    print(f"Радіус: {r}")
    print(f"Діаметр: {diameter(r)}")
    print(f"Довжина: {circumference(r):.4f}")
    print(f"Площа: {area(r):.4f}")
