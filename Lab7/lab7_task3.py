"""
Лабораторна робота №7 — Завдання 3
Інкапсуляція: property з getter, setter, deleter.
"""


class StudentKod:
    """Приклад з методички — приватне поле __kod."""

    def __init__(self, name: str, kod: int):
        self.name = name
        self.__kod = kod

    @property
    def kod(self) -> int:
        return self.__kod

    @kod.setter
    def kod(self, kod: int) -> None:
        if not isinstance(kod, int):
            raise TypeError("Код має бути цілим числом")
        if len(str(kod)) != 4:
            raise Exception("Потрібно 4 цифри")
        self.__kod = kod

    @kod.deleter
    def kod(self) -> None:
        del self.__kod


class Student:
    """Студент з приватним полем балу за предмет (zalik)."""

    def __init__(self, surname: str, zalik: float = 0):
        self.surname = surname
        self.__zalik = zalik

    @property
    def zalik(self) -> str:
        """Повертає 'зарах' або 'незарах' залежно від балу."""
        return "зарах" if self.__zalik > 4 else "незарах"

    @zalik.setter
    def zalik(self, value) -> None:
        if isinstance(value, (list, tuple)):
            self.__zalik = sum(value)
        else:
            self.__zalik = float(value)

    @zalik.deleter
    def zalik(self) -> None:
        self.__zalik = 0


if __name__ == "__main__":
    record = StudentKod("Petriv", 4501)
    print("StudentKod:", record.name, record.kod)

    stud = Student("Коваленко")
    stud.zalik = 5
    print(f"\n{stud.surname}: {stud.zalik}")

    stud.zalik = [4, 5, 5]
    print(f"{stud.surname} (сума балів): {stud.zalik}")

    stud.zalik = 3
    print(f"{stud.surname} (низький бал): {stud.zalik}")

    del stud.zalik
    print(f"{stud.surname} (після deleter): {stud.zalik}")
