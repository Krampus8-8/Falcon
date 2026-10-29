# 11 практическая. Словари. Задачи Dict1-Dict15


def read_dict(label="словаря"):
    """Читает N пар (ключ - строка, значение - целое) и возвращает словарь."""
    n = int(input(f"Количество пар {label} N: "))
    d = {}
    for i in range(n):
        key = input(f"Ключ {i + 1}: ")
        value = int(input(f"Значение {i + 1}: "))
        d[key] = value
    return d


while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 11. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("1  - Dict1  (Число пар и все ключи)")
    print("4  - Dict4  (Увеличить значение или добавить пару)")
    print("6  - Dict6  (Сумма всех значений)")
    print("10 - Dict10 (Пары «название: цена»)")
    print("11 - Dict11 (Счётчик слов)")
    print("--- Делаем сами ---")
    print("2  - Dict2  (Значение по ключу через in)")
    print("3  - Dict3  (Значение через get)")
    print("5  - Dict5  (Удалить ключ через pop)")
    print("7  - Dict7  (Ключ с наибольшим значением)")
    print("8  - Dict8  (Есть ли значение V)")
    print("9  - Dict9  (Слияние словарей через update)")
    print("12 - Dict12 [СЛОЖНОЕ] (Обращённый словарь)")
    print("13 - Dict13 [СЛОЖНОЕ] (Склад: стоимость и самый дорогой)")
    print("14 - Dict14 [СЛОЖНОЕ] (Удалить пары меньше V)")
    print("15 - Dict15 (Добавить пары без update)")
    print("0  - Выход")
    print("=" * 60)

    choice = input("Введите номер задачи: ").strip()

    if choice == "0":
        print("Программа завершена.")
        break

    elif choice == "1":
        # Dict1. Число пар и все ключи в порядке добавления.
        d = read_dict()
        print(len(d))
        for key in d:
            print(key)

    elif choice == "2":
        # Dict2. Значение ключа K или «нет такого ключа».
        d = read_dict()
        k = input("Ключ K: ")
        if k in d:
            print(d[k])
        else:
            print("нет такого ключа")

    elif choice == "3":
        # Dict3. Значение ключа K через get с default 0.
        d = read_dict()
        k = input("Ключ K: ")
        print(d.get(k, 0))

    elif choice == "4":
        # Dict4. Если K есть, увеличить на V, иначе добавить пару.
        d = read_dict()
        k = input("Ключ K: ")
        v = int(input("Число V: "))
        if k in d:
            d[k] += v
        else:
            d[k] = v
        print(d[k])

    elif choice == "5":
        # Dict5. Удалить ключ K через pop с default, вывести размер.
        d = read_dict()
        k = input("Ключ K: ")
        d.pop(k, None)
        print(len(d))

    elif choice == "6":
        # Dict6. Сумма всех значений обходом по values.
        d = read_dict()
        total = 0
        for value in d.values():
            total += value
        print(total)

    elif choice == "7":
        # Dict7. Ключ с наибольшим значением.
        d = read_dict()
        best = None
        for key in d:
            if best is None or d[key] > d[best]:
                best = key
        print(best)

    elif choice == "8":
        # Dict8. Встречается ли V среди значений.
        d = read_dict()
        v = int(input("Число V: "))
        print(v in d.values())

    elif choice == "9":
        # Dict9. Слить второй словарь в первый через update.
        first = read_dict("первого словаря")
        second = read_dict("второго словаря")
        common = None
        for key in second:
            if key in first:
                common = key
        first.update(second)
        print(len(first))
        print(first[common])

    elif choice == "10":
        # Dict10. Каждая пара строкой «название: цена».
        d = read_dict()
        for name, price in d.items():
            print(f"{name}: {price}")

    elif choice == "11":
        # Dict11. Словарь-счётчик слов.
        n = int(input("Количество слов N: "))
        counts = {}
        for i in range(n):
            word = input(f"Слово {i + 1}: ")
            counts[word] = counts.get(word, 0) + 1
        for word, count in counts.items():
            print(word, count)

    elif choice == "12":
        # Dict12. Обращённый словарь: значение -> ключ.
        d = read_dict()
        inverted = {}
        for key, value in d.items():
            inverted[value] = key
        for value, key in inverted.items():
            print(value, key)

    elif choice == "13":
        # Dict13. Склад: название -> [цена, количество].
        n = int(input("Количество предметов N: "))
        stock = {}
        for i in range(n):
            name = input(f"Название {i + 1}: ")
            price = int(input("Цена: "))
            qty = int(input("Количество: "))
            stock[name] = [price, qty]
        total = 0
        best = None
        best_cost = -1
        for name in stock:
            price, qty = stock[name]
            cost = price * qty
            total += cost
            if cost > best_cost:
                best_cost = cost
                best = name
        print("Стоимость склада:", total)
        print("Самый дорогой:", best)

    elif choice == "14":
        # Dict14. Удалить пары со значением меньше V.
        d = read_dict()
        v = int(input("Число V: "))
        for key in list(d):
            if d[key] < v:
                del d[key]
        print(len(d))

    elif choice == "15":
        # Dict15. Добавить пары второго словаря без update.
        first = read_dict("первого словаря")
        second = read_dict("второго словаря")
        ignored = 0
        for key, value in second.items():
            if key in first:
                ignored += 1
            else:
                first[key] = value
        print(len(first))
        print("Проигнорировано:", ignored)

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
