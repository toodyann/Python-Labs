"""
Лабораторна робота №7 — Завдання 1
Методи екземпляра, класу (@classmethod) та статичні (@staticmethod).
"""


class BankAccount:
    """Банківський рахунок — приклад різних типів методів."""

    bank_name = "KNU Bank"
    _accounts_count = 0

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
        BankAccount._accounts_count += 1

    def deposit(self, amount: float) -> float:
        """Метод екземпляра: поповнення рахунку."""
        if not self.validate_amount(amount):
            raise ValueError("Сума має бути невід'ємним числом")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """Метод екземпляра: зняття коштів."""
        if not self.validate_amount(amount):
            raise ValueError("Сума має бути невід'ємним числом")
        if amount > self.balance:
            raise ValueError("Недостатньо коштів")
        self.balance -= amount
        return self.balance

    @classmethod
    def from_dict(cls, data: dict) -> "BankAccount":
        """Метод класу: створення рахунку зі словника."""
        return cls(data["owner"], data.get("balance", 0.0))

    @classmethod
    def accounts_count(cls) -> int:
        """Метод класу: кількість створених рахунків."""
        return cls._accounts_count

    @staticmethod
    def validate_amount(amount) -> bool:
        """Статичний метод: перевірка коректності суми."""
        return isinstance(amount, (int, float)) and amount >= 0


if __name__ == "__main__":
    acc1 = BankAccount("Іваненко", 1000)
    acc1.deposit(500)
    acc1.withdraw(200)
    print(f"{acc1.owner}: баланс = {acc1.balance}")

    acc2 = BankAccount.from_dict({"owner": "Петренко", "balance": 300})
    print(f"{acc2.owner}: баланс = {acc2.balance}")

    print("Банк:", BankAccount.bank_name)
    print("Рахунків створено:", BankAccount.accounts_count())
    print("validate_amount(-10):", BankAccount.validate_amount(-10))
    print("validate_amount(50):", BankAccount.validate_amount(50))
