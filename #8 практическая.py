#8 практическая

while True:
    print("\n" + "="*70)
    print("ВЫБЕРИТЕ НОМЕР ЗАДАЧИ ДЛЯ ПРОВЕРКИ:")
    print("--- Разбираем вместе ---")
    print("16 - List16 (Сумма, минимум и максимум через агрегаторы)")
    print("18 - List18 (Сортировка на месте по убыванию через sort)")
    print("20 - List20 (Генератор списка квадратов чисел)")
    print("24 - List24 (Сортировка строк по длине и самая длинная строка)")
    print("27 - List27 (Таблица раундов: сортировка списка списков по колонке)")
    print("--- Самостоятельная работа ---")
    print("17 - List17 (Вывод по возрастанию без изменения оригинала)")
    print("19 - List19 (Сортировка по длине и поиск максимума с key)")
    print("21 - List21 (Генератор-фильтр положительных элементов и их len)")
    print("22 - List22 (Генератор умножения на D и подсчет вхождений D)")
    print("23 - List23 (Сортировка по убыванию модуля key=abs)")
    print("25 - List25 [HARD] (Поиск второго по величине элемента)")
    print("26 - List26 (Элементы больше среднего значения списка)")
    print("28 - List28 (Фильтр строк, начинающихся на заданную букву)")
    print("29 - List29 [HARD] (K наибольших элементов по убыванию через срез)")
    print("30 - List30 (Генератор списка длин строк и их общая сумма)")
    print("0  - Выход из программы")
    print("="*70)
    
    choice = input("Введите номер задания: ").strip()
    
    if choice == "0":
        print("Программа завершена. Продвинутая работа со списками освоена!")
        break
        
    elif choice == "16":
        print("\n--- Выполняется задание List16 ---")
        n = int(input("Введите количество элементов N (>= 1): "))
        a = [int(input(f"Элемент {i+1}: ")) for i in range(n)]
        print(f"Сумма: {sum(a)}")
        print(f"Минимум: {min(a)}")
        print(f"Максимум: {max(a)}")
        
    elif choice == "17":
        print("\n--- Выполняется задание List17 ---")
        n = int(input("Введите количество элементов N: "))
        a = [int(input(f"Элемент {i+1}: ")) for i in range(n)]
        print("По возрастанию:", sorted(a))
        print("Исходный список без изменений:", a)
        
    elif choice == "18":
        print("\n--- Выполняется задание List18 ---")
        n = int(input("Введите количество элементов N: "))
        a = [int(input(f"Элемент {i+1}: ")) for i in range(n)]
        a.sort(reverse=True)
        print("Отсортированный список на месте:", a)
        print(f"Длина списка: {len(a)}")
        
    elif choice == "19":
        print("\n--- Выполняется задание List19 ---")
        n = int(input("Введите количество строк N: "))
        s = [input(f"Строка {i+1}: ") for i in range(n)]
        print("Строки по возрастанию длины:", sorted(s, key=len))
        print("Самая длинная строка:", max(s, key=len))
        
    elif choice == "20":
        print("\n--- Выполняется задание List20 ---")
        n = int(input("Введите количество элементов N: "))
        a = [int(input(f"Элемент {i+1}: ")) for i in range(n)]
        sq = [x * x for x in a]
        print("Список квадратов:", sq)
        print("Сумма квадратов:", sum(sq))
        
    elif choice == "21":
        print("\n--- Выполняется задание List21 ---")
        n = int(input("Введите количество элементов N: "))
        a = [int(input(f"Элемент {i+1}: ")) for i in range(n)]
        pos = [x for x in a if x > 0]
        print("Только положительные элементы:", pos)
        print(f"Их количество: {len(pos)}")
        
    elif choice == "22":
        print("\n--- Выполняется задание List22 ---")
        n = int(input("Введите количество элементов N: "))
        a = [int(input(f"Элемент {i+1}: ")) for i in range(n)]
        d = int(input("Введите число D для операции: "))
        multiplied = [x * d for x in a]
        count_d = len([x for x in a if x == d])
        print(f"Элементы, умноженные на {d}:", multiplied)
        print(f"Количество элементов, изначально равных {d}: {count_d}")
        
    elif choice == "23":
        print("\n--- Выполняется задание List23 ---")
        n = int(input("Введите количество элементов N: "))
        a = [int(input(f"Элемент {i+1}: ")) for i in range(n)]
        print("По убыванию модуля:", sorted(a, key=abs, reverse=True))
        
    elif choice == "24":
        print("\n--- Выполняется задание List24 ---")
        n = int(input("Введите количество строк N: "))
        s = [input(f"Строка {i+1}: ") for i in range(n)]
        print("Строки по возрастанию длины:", sorted(s, key=len))
        print("Самая длинная строка:", max(s, key=len))
        
    elif choice == "25":
        print("\n--- Выполняется задание List25 [HARD] ---")
        n = int(input("Введите количество РАЗЛИЧНЫХ элементов N (>= 2): "))
        a = [int(input(f"Элемент {i+1}: ")) for i in range(n)]
        ordered = sorted(a, reverse=True)
        print(f"Второй по величине элемент: {ordered[1]}")
        
    elif choice == "26":
        print("\n--- Выполняется задание List26 ---")
        n = int(input("Введите количество элементов N: "))
        a = [int(input(f"Элемент {i+1}: ")) for i in range(n)]
        avg = sum(a) / len(a)
        above_avg = [x for x in a if x > avg]
        print(f"Среднее арифметическое списка: {avg:.1f}")
        print("Элементы больше среднего:", above_avg)
        
    elif choice == "27":
        print("\n--- Выполняется задание List27 ---")
        n = int(input("Введите количество раундов N: "))
        rows = []
        for i in range(n):
            print(f"Раунд {i+1}:")
            x = float(input("  Урон героя: "))
            y = float(input("  Урон врага: "))
            rows.append([x, y])
        rows.sort(key=lambda r: r[0], reverse=True)
        print("Таблица раундов по убыванию урона героя:")
        for r in rows:
            print(r)
        print("Лучший раунд (макс. урон героя):", rows[0])
        
    elif choice == "28":
        print("\n--- Выполняется задание List28 ---")
        n = int(input("Введите количество строк N: "))
        s = [input(f"Строка {i+1}: ") for i in range(n)]
        letter = input("Введите искомую начальную букву: ").strip()
        filtered_strings = [string for string in s if string and string[0] == letter]
        print(f"Строки, начинающиеся на букву '{letter}':", filtered_strings)
        
    elif choice == "29":
        print("\n--- Выполняется задание List29 [HARD] ---")
        n = int(input("Введите количество элементов N: "))
        a = [int(input(f"Элемент {i+1}: ")) for i in range(n)]
        k = int(input(f"Сколько наибольших элементов вывести (K <= {n}): "))
        top_k = sorted(a, reverse=True)[:k]
        print(f"{k} наибольших элементов по убыванию:", top_k)
        
    elif choice == "30":
        print("\n--- Выполняется задание List30 ---")
        n = int(input("Введите количество строк N: "))
        s = [input(f"Строка {i+1}: ") for i in range(n)]
        lengths = [len(string) for string in s]
        print("Список длин строк:", lengths)
        print("Суммарная длина всех строк:", sum(lengths))
        
    else:
        print("Неверный ввод! Пожалуйста, выберите номер из списка.")
        
    input("\nНажмите Enter для возврата в меню...")
