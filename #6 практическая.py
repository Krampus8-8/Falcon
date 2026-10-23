#6 практическая

while True:
    print("\n" + "="*50)
    print("ВЫБЕРИТЕ НОМЕР ЗАДАЧИ ДЛЯ ПРОВЕРКИ:")
    print("--- Разбираем вместе ---")
    print("1  - Err1 (Прочитать целое число или 'Ошибка ввода')")
    print("3  - Err3 (Частное двух чисел с защитой от 0 и букв)")
    print("4  - Err4 (Использование блоков else и finally)")
    print("8  - Err8 (Подсчет суммы и пропусков до пустой строки)")
    print("10 - Err10 (Ввод пункта меню от 1 до 5)")
    print("--- Делаем сами ---")
    print("2  - Err2 (Деление на ноль с округлением до 1 знака)")
    print("5  - Err5 (Вывод символа строки по индексу)")
    print("6  - Err6 (Символ по индексу с полной защитой)")
    print("7  - Err7 (Универсальное чтение целого числа)")
    print("9  - Err9 (Проверка возраста через raise)")
    print("11 - Err11 (Обработка двух ошибок одним кортежем)")
    print("12 - Err12 (Вывод текста исключения и его типа через as e)")
    print("--- Повторение с защитой ---")
    print("81 - Begin8_protect (Среднее арифметическое)")
    print("31 - If3_protect (Модификация числа)")
    print("51 - While11_protect (Минимальное K для суммы >= N)")
    print("0  - Выход из программы")
    print("="*50)
    
    choice = input("Введите номер задания: ").strip()
    
    if choice == "0":
        print("Программа завершена. Защита кода выстроена отлично!")
        break
        
    elif choice == "1":
        print("\n--- Выполняется задание Err1 ---")
        try:
            number = int(input("Введите целое число: "))
            print(f"Успешно прочитано число: {number}")
        except ValueError:
            print("Ошибка ввода")
            
    elif choice == "2":
        print("\n--- Выполняется задание Err2 ---")
        try:
            a = int(input("Введите делимое (A): "))
            b = int(input("Введите делитель (B): "))
            print(f"Частное: {a / b:.1f}")
        except ZeroDivisionError:
            print("Делить на ноль нельзя")
            
    elif choice == "3":
        print("\n--- Выполняется задание Err3 ---")
        try:
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            print(f"Результат деления: {a / b}")
        except ValueError:
            print("Ошибка ввода")
        except ZeroDivisionError:
            print("Делить на ноль нельзя")
            
    elif choice == "4":
        print("\n--- Выполняется задание Err4 ---")
        try:
            n = int(input("Введите целое число N: "))
            result = 100 / n
        except ValueError:
            print("Ошибка ввода")
        except ZeroDivisionError:
            print("Делить на ноль нельзя")
        else:
            print(f"Успех! 100 / N = {result}")
        finally:
            print("Вычисление завершено")
            
    elif choice == "5":
        print("\n--- Выполняется задание Err5 ---")
        text = input("Введите строку: ")
        try:
            index = int(input("Введите индекс символа: "))
            print(f"Символ под индексом {index}: {text[index]}")
        except IndexError:
            print("Нет такого символа")
            
    elif choice == "6":
        print("\n--- Выполняется задание Err6 ---")
        text = input("Введите строку: ")
        try:
            index = int(input("Введите индекс символа: "))
            print(f"Символ: {text[index]}")
        except ValueError:
            print("Ошибка ввода")
        except IndexError:
            print("Нет такого символа")
            
    elif choice == "7":
        print("\n--- Выполняется задание Err7 ---")
        print("Вводите данные, пока программа не примет целое число.")
        while True:
            try:
                number = int(input("Введите число: "))
                break
            except ValueError:
                print("Это не число. Попробуй ещё:")
        print(f"Получено число: {number}")
        
    elif choice == "8":
        print("\n--- Выполняется задание Err8 ---")
        print("Вводите целые числа (для окончания нажмите Enter на пустой строке):")
        total = 0
        skipped = 0
        while True:
            line = input()
            if line == "":
                break
            try:
                total += int(line)
            except ValueError:
                skipped += 1
                print("Пропущено: не число")
        print(f"Сумма корректных чисел: {total}")
        print(f"Количество пропущенных строк: {skipped}")
        
    elif choice == "9":
        print("\n--- Выполняется задание Err9 ---")
        try:
            age = int(input("Введите возраст (от 0 до 120): "))
            if age < 0 or age > 120:
                raise ValueError("Возраст вне допустимого диапазона")
            print(f"Принято: {age}")
        except ValueError as e:
            print(f"Отклонено: {e}")
            
    elif choice == "10":
        print("\n--- Выполняется задание Err10 ---")
        print("Выберите пункт меню (от 1 до 5):")
        while True:
            try:
                choice_menu = int(input())
            except ValueError:
                print("Введите число")
                continue
            if 1 <= choice_menu <= 5:
                break
            print("Такого пункта нет")
        print(f"Выбран пункт меню: {choice_menu}")
        
    elif choice == "11":
        print("\n--- Выполняется задание Err11 ---")
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            result = a / b
        except (ValueError, ZeroDivisionError):
            print("Посчитать не удалось")
        else:
            print(f"Частное с двумя знаками: {result:.2f}")
            
    elif choice == "12":
        print("\n--- Выполняется задание Err12 ---")
        try:
            number = int(input("Введите целое число: "))
            print(f"Успешный ввод: {number}")
        except ValueError as e:
            print(f"Текст исключения: {e}")
            print(f"Тип исключения: {type(e)}")
            
    elif choice == "81":
        print("\n--- Выполняется Повторение: Begin8_protect ---")
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            print(f"Среднее арифметическое: {(a + b) / 2}")
        except ValueError:
            print("Ошибка ввода")
            
    elif choice == "31":
        print("\n--- Выполняется Повторение: If3_protect ---")
        try:
            number = int(input("Введите целое число: "))
            if number > 0:
                number += 1
            elif number < 0:
                number -= 2
            else:
                number = 10
            print(f"Результат модификации: {number}")
        except ValueError:
            print("Ошибка ввода")
            
    elif choice == "51":
        print("\n--- Выполняется Повторение: While11_protect ---")
        try:
            n = int(input("Введите целое число N (> 1): "))
            if n <= 1:
                print("Ошибка: число должно быть больше 1 по условию исходной задачи.")
            else:
                total = 0
                k = 0
                while total < n:
                    k += 1
                    total += k
                print(f"Наименьшее K: {k}")
                print(f"Сумма: {total}")
        except ValueError:
            print("Ошибка ввода")
            
    else:
        print("Неверный ввод! Пожалуйста, выберите номер из списка.")
        
    input("\nНажмите Enter для возврата в меню...")
