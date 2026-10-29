# 6 практическая. Ошибки и защита. Задачи Err1-Err12 и повторение с защитой

while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 6. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("1  - Err1  (Прочитать целое число)")
    print("3  - Err3  (Частное двух чисел с двумя проверками)")
    print("4  - Err4  (try / else / finally)")
    print("8  - Err8  (Сумма чисел до пустой строки)")
    print("10 - Err10 (Пункт меню от 1 до 5)")
    print("--- Делаем сами ---")
    print("2  - Err2  (Частное с одним знаком, деление на ноль)")
    print("5  - Err5  (Символ строки по индексу)")
    print("6  - Err6  (Символ по индексу, две ветки ошибок)")
    print("7  - Err7  (Читать, пока не введут целое число)")
    print("9  - Err9  [СЛОЖНОЕ] (Проверка возраста через raise)")
    print("11 - Err11 (Две ошибки одним кортежем)")
    print("12 - Err12 [СЛОЖНОЕ] (Текст и тип исключения)")
    print("--- Повторение с защитой ---")
    print("0  - Выход")
    print("=" * 60)

    choice = input("Введите номер задачи: ").strip()

    if choice == "0":
        print("Программа завершена.")
        break

    elif choice == "1":
        # Err1. Прочитать целое число и вывести его. Если не число: "Ошибка ввода".
        try:
            number = int(input("Целое число: "))
            print(number)
        except ValueError:
            print("Ошибка ввода")

    elif choice == "2":
        # Err2. Частное двух целых с одним знаком. Деление на ноль: "Делить на ноль нельзя".
        a = int(input("Делимое: "))
        b = int(input("Делитель: "))
        try:
            print(f"{a / b:.1f}")
        except ZeroDivisionError:
            print("Делить на ноль нельзя")

    elif choice == "3":
        # Err3. Частное двух целых. Не число: "Ошибка ввода", ноль: "Делить на ноль нельзя".
        try:
            a = int(input("Делимое: "))
            b = int(input("Делитель: "))
            print(a / b)
        except ValueError:
            print("Ошибка ввода")
        except ZeroDivisionError:
            print("Делить на ноль нельзя")

    elif choice == "4":
        # Err4. В else вывести 100 / n, в finally "Вычисление завершено".
        try:
            n = int(input("Целое число: "))
            result = 100 / n
        except ValueError:
            print("Ошибка ввода")
        except ZeroDivisionError:
            print("Делить на ноль нельзя")
        else:
            print(result)
        finally:
            print("Вычисление завершено")

    elif choice == "5":
        # Err5. Строка и индекс. Если индекса нет: "Нет такого символа".
        word = input("Строка: ")
        index = int(input("Индекс: "))
        try:
            print(word[index])
        except IndexError:
            print("Нет такого символа")

    elif choice == "6":
        # Err6. Как Err5, но нечисловой индекс: "Ошибка ввода".
        word = input("Строка: ")
        try:
            index = int(input("Индекс: "))
            print(word[index])
        except ValueError:
            print("Ошибка ввода")
        except IndexError:
            print("Нет такого символа")

    elif choice == "7":
        # Err7. Читать ввод, пока не будет введено целое число.
        while True:
            try:
                number = int(input("Целое число: "))
                break
            except ValueError:
                print("Это не число. Попробуй ещё:")
        print(number)

    elif choice == "8":
        # Err8. Читать числа до пустой строки, нечисловые пропускать со счётом.
        total = 0
        skipped = 0
        print("Вводите целые числа, пустая строка - конец:")
        while True:
            line = input()
            if line == "":
                break
            try:
                total += int(line)
            except ValueError:
                print("Пропущено: не число")
                skipped += 1
        print("Сумма:", total)
        print("Пропущено строк:", skipped)

    elif choice == "9":
        # Err9. Возраст от 0 до 120, иначе raise ValueError и вывести "Отклонено:".
        try:
            age = int(input("Возраст: "))
            if age < 0 or age > 120:
                raise ValueError("Возраст вне допустимого диапазона")
            print("Принято:", age)
        except ValueError as e:
            print("Отклонено:", e)

    elif choice == "10":
        # Err10. Пункт меню от 1 до 5 с перечитыванием.
        while True:
            try:
                item = int(input("Пункт меню (1-5): "))
            except ValueError:
                print("Введите число")
                continue
            if 1 <= item <= 5:
                break
            print("Такого пункта нет")
        print("Выбран пункт:", item)

    elif choice == "11":
        # Err11. Обе ошибки одним кортежем, при успехе частное с двумя знаками.
        try:
            a = float(input("Первое число: "))
            b = float(input("Второе число: "))
            result = a / b
        except (ValueError, ZeroDivisionError):
            print("Посчитать не удалось")
        else:
            print(f"{result:.2f}")

    elif choice == "12":
        # Err12. При ошибке вывести текст исключения и его тип.
        try:
            number = int(input("Целое число: "))
        except ValueError as e:
            print(e)
            print(type(e))
        else:
            print(number)

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
