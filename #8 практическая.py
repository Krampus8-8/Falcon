# 8 практическая. Списки глубже: сортировка и генераторы. Задачи List16-List30


def read_numbers():
    n = int(input("Количество элементов N: "))
    numbers = []
    for i in range(n):
        numbers.append(int(input(f"Элемент {i + 1}: ")))
    return numbers


def read_strings():
    n = int(input("Количество строк N: "))
    strings = []
    for i in range(n):
        strings.append(input(f"Строка {i + 1}: "))
    return strings


while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 8. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("16 - List16 (Сумма, минимум и максимум)")
    print("18 - List18 (Сортировка на месте по убыванию)")
    print("20 - List20 (Генератор квадратов)")
    print("24 - List24 (Строки по длине и самая длинная)")
    print("--- Делаем сами ---")
    print("17 - List17 (По возрастанию без изменения оригинала)")
    print("19 - List19 (Строки по длине и самая длинная через max)")
    print("21 - List21 (Только положительные и их количество)")
    print("22 - List22 (Умножить на D и посчитать равные D)")
    print("23 - List23 (По убыванию модуля)")
    print("25 - List25 [HARD] (Второй по величине)")
    print("0  - Выход")
    print("=" * 60)

    choice = input("Введите номер задачи: ").strip()

    if choice == "0":
        print("Программа завершена.")
        break

    elif choice == "16":
        # List16. Сумма, минимум и максимум через sum, min, max.
        a = read_numbers()
        print("Сумма:", sum(a))
        print("Минимум:", min(a))
        print("Максимум:", max(a))

    elif choice == "17":
        # List17. По возрастанию (sorted), затем исходный список без изменений.
        a = read_numbers()
        print(sorted(a))
        print(a)

    elif choice == "18":
        # List18. Отсортировать на месте по убыванию, вывести список и длину.
        a = read_numbers()
        a.sort(reverse=True)
        print(a)
        print("Длина:", len(a))

    elif choice == "19":
        # List19. Строки по возрастанию длины и самая длинная (max с key).
        s = read_strings()
        print(sorted(s, key=len))
        print("Самая длинная:", max(s, key=len))

    elif choice == "20":
        # List20. Генератором список квадратов и сумма квадратов.
        a = read_numbers()
        squares = [x * x for x in a]
        print(squares)
        print("Сумма квадратов:", sum(squares))

    elif choice == "21":
        # List21. Генератором с фильтром только положительные и их количество.
        a = read_numbers()
        positive = [x for x in a if x > 0]
        print(positive)
        print("Количество:", len(positive))

    elif choice == "22":
        # List22. Элементы, умноженные на D, и количество элементов, равных D.
        a = read_numbers()
        d = int(input("D: "))
        multiplied = [x * d for x in a]
        equal_count = len([x for x in a if x == d])
        print(multiplied)
        print("Равных D:", equal_count)

    elif choice == "23":
        # List23. По убыванию модуля.
        a = read_numbers()
        print(sorted(a, key=abs, reverse=True))

    elif choice == "24":
        # List24. Строки по возрастанию длины и самая длинная.
        s = read_strings()
        print(sorted(s, key=len))
        print("Самая длинная:", max(s, key=len))

    elif choice == "25":
        # List25. Второй по величине элемент (числа различные).
        a = read_numbers()
        print("Второй по величине:", sorted(a, reverse=True)[1])

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
