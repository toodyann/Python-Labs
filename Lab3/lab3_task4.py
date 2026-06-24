"""
Лабораторна робота №3 — Завдання 4
Магазин: купівля товарів за ціною за кг.
"""

PRODUCTS = [
    ["Apple", 3.7],
    ["Banane", 9.4],
    ["Orange", 5.2],
    ["Grapes", 12.0],
    ["Pear", 4.8],
]


def show_catalog(products: list) -> None:
    print("Наявний товар:")
    for name, price in products:
        print(f"  {name}: {price} за кг")


def price_map(products: list) -> dict:
    return {name: price for name, price in products}


def shop() -> None:
    catalog = price_map(PRODUCTS)
    show_catalog(PRODUCTS)

    purchases: list[tuple[str, float, float]] = []
    total = 0.0

    while True:
        name = input("\nНазва товару (або 'ок' для завершення): ").strip()
        if name.lower() == "ок":
            break
        if name not in catalog:
            print("Такого товару немає")
            continue

        try:
            amount = float(input("Кількість (кг): "))
        except ValueError:
            print("Введіть число")
            continue

        cost = catalog[name] * amount
        purchases.append((name, amount, cost))
        total += cost
        print(f"Додано: {name} — {amount} кг, сума {cost:.2f}")

    print("\n=== Чек ===")
    for name, amount, cost in purchases:
        print(f"{name}: {amount} кг -> {cost:.2f}")
    print(f"Загальна сума: {total:.2f}")


if __name__ == "__main__":
    shop()
