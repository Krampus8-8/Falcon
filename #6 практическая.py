# 6 практическая. Ошибки и защита. Задачи Err1-Err12 и повторение с защитой

while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 6. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("1  - Err1  (Прочитать целое число)")
    print("3  - Err3  (Частное двух чисел с двумя проверками)")
    print("4  - Err4  (try / else / finally)")
    print("--- Делаем сами ---")
    print("2  - Err2  (Частное с одним знаком, деление на ноль)")
    print("5  - Err5  (Символ строки по индексу)")
    print("6  - Err6  (Символ по индексу, две ветки ошибок)")
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

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
