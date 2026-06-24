"""
Лабораторна робота №2 — Завдання 3
Меню для роботи зі списком.
"""

MENU = """My menu
1: create list
2: preview
3: add element
4: delete element
5: pass
6: exit"""


def run_menu() -> None:
    my_list: list | None = None

    while True:
        print(MENU)
        try:
            choice = int(input("Оберіть пункт меню: "))
        except ValueError:
            print("Необхідно задати число")
            continue

        if choice == 1:
            my_list = []
            print("Done")
        elif choice == 2:
            if my_list is None:
                print("Спочатку створіть список (пункт 1)")
            else:
                print(my_list)
        elif choice == 3:
            if my_list is None:
                print("Спочатку створіть список (пункт 1)")
            else:
                print("Element:")
                element = input()
                my_list.append(element)
        elif choice == 4:
            if my_list is None:
                print("Спочатку створіть список (пункт 1)")
            else:
                try:
                    index = int(input("Порядковий номер для видалення: "))
                    del my_list[index]
                except (ValueError, IndexError):
                    print("Невірний індекс")
        elif choice == 5:
            pass
        elif choice == 6:
            break
        else:
            print("Дане число не входить у пункти меню")


if __name__ == "__main__":
    run_menu()
