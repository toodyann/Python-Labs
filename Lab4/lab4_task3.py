"""
Лабораторна робота №4 — Завдання 3
Курси валют ПриватБанку
"""

import json

import requests

API_URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"


def load_rates():
    """Завантажити курси з API та підготувати структуру даних."""
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    raw_data = response.json()

    rates = {}
    for item in raw_data:
        currency = item["ccy"]
        rates[currency] = {
            "buy": float(item["buy"]),
            "sale": float(item["sale"]),
            "base": item["base_ccy"],
        }
    return rates


def sell_currency(rates, currency, amount):
    """
    Продаж валюти банку.
    Клієнт продає валюту — банк купує за курсом 'buy'.
    """
    currency = currency.strip().upper()
    aliases = {
        "EUR": "EUR",
        "EURO": "EUR",
        "ЄВРО": "EUR",
        "USD": "USD",
        "DOLLAR": "USD",
        "ДОЛАР": "USD",
    }

    code = aliases.get(currency)
    if code is None:
        raise ValueError("Доступні валюти: EUR (євро) або USD (долар)")

    if code not in rates:
        raise ValueError(f"Курс для {code} не знайдено")

    uah = amount * rates[code]["buy"]
    return uah


def main():
    rates = load_rates()
    print("Курси валют (ПриватБанк):")
    for code, info in rates.items():
        print(f"  {code}: купівля {info['buy']}, продаж {info['sale']} {info['base']}")

    currency = input("\nЯку валюту продаєте (EUR/USD)? ").strip()
    amount = float(input("Сума валюти для продажу: "))

    result = sell_currency(rates, currency, amount)
    print(f"Ви отримаєте: {result:.2f} грн")


if __name__ == "__main__":
    main()
