# 4 практическая. Циклы for. Задачи For1-For15

while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 4. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("1  - For1  (Вывести N раз число K)")
    print("3  - For3  (Числа между A и B по убыванию)")
    print("7  - For7  (Сумма чисел от A до B)")
    print("10 - For10 (Сумма 1 + 1/2 + ... + 1/N)")
    print("14 - For14 (Квадрат N через сумму нечётных)")
    print("--- Делаем сами ---")
    print("2  - For2  (Числа от A до B по возрастанию и их количество)")
    print("4  - For4  (Стоимость 1..10 кг конфет)")
    print("5  - For5  [СЛОЖНОЕ] (Стоимость 0.1..1 кг)")
    print("6  - For6  [СЛОЖНОЕ] (Стоимость 1.2..2 кг)")
    print("8  - For8  (Произведение чисел от A до B)")
    print("9  - For9  (Сумма квадратов от A до B)")
    print("11 - For11 (Сумма квадратов от N до 2N)")
    print("12 - For12 (Произведение 1.1 * 1.2 * ...)")
    print("13 - For13 [СЛОЖНОЕ] (1.1 - 1.2 + 1.3 - ...)")
    print("15 - For15 (A в степени N)")
    print("0  - Выход")
    print("=" * 60)

    choice = input("Введите номер задачи: ").strip()

    if choice == "0":
        print("Программа завершена.")
        break

    elif choice == "1":
        # For1. Даны K и N (N > 0). Вывести N раз число K.
        k = int(input("K: "))
        n = int(input("N: "))
        for _ in range(n):
            print(k)

    elif choice == "2":
        # For2. Вывести по возрастанию числа от A до B (включая A и B) и их количество.
        a = int(input("A: "))
        b = int(input("B (больше A): "))
        amount = 0
        for x in range(a, b + 1):
            print(x)
            amount += 1
        print("Количество N =", amount)

    elif choice == "3":
        # For3. Вывести по убыванию числа между A и B (не включая A и B) и их количество.
        a = int(input("A: "))
        b = int(input("B (больше A): "))
        amount = 0
        for x in range(b - 1, a, -1):
            print(x)
            amount += 1
        print("Количество N =", amount)

    elif choice == "4":
        # For4. Цена 1 кг конфет. Вывести стоимость 1, 2, ..., 10 кг.
        price = float(input("Цена 1 кг: "))
        for kg in range(1, 11):
            print(f"{kg} кг: {price * kg}")

    elif choice == "5":
        # For5. Стоимость 0.1, 0.2, ..., 1 кг конфет.
        price = float(input("Цена 1 кг: "))
        for i in range(1, 11):
            kg = i / 10
            print(f"{kg} кг: {price * kg}")

    elif choice == "6":
        # For6. Стоимость 1.2, 1.4, ..., 2 кг конфет.
        price = float(input("Цена 1 кг: "))
        for i in range(12, 21, 2):
            kg = i / 10
            print(f"{kg} кг: {price * kg}")

    elif choice == "7":
        # For7. Сумма всех целых чисел от A до B включительно.
        a = int(input("A: "))
        b = int(input("B (больше A): "))
        total = 0
        for x in range(a, b + 1):
            total += x
        print("Сумма =", total)

    elif choice == "8":
        # For8. Произведение всех целых чисел от A до B включительно.
        a = int(input("A: "))
        b = int(input("B (больше A): "))
        product = 1
        for x in range(a, b + 1):
            product *= x
        print("Произведение =", product)

    elif choice == "9":
        # For9. Сумма квадратов всех целых чисел от A до B включительно.
        a = int(input("A: "))
        b = int(input("B (больше A): "))
        total = 0
        for x in range(a, b + 1):
            total += x ** 2
        print("Сумма квадратов =", total)

    elif choice == "10":
        # For10. Сумма 1 + 1/2 + 1/3 + ... + 1/N.
        n = int(input("N: "))
        total = 0.0
        for i in range(1, n + 1):
            total += 1 / i
        print("Сумма =", total)

    elif choice == "11":
        # For11. Сумма N^2 + (N+1)^2 + ... + (2N)^2.
        n = int(input("N: "))
        total = 0
        for x in range(n, 2 * n + 1):
            total += x ** 2
        print("Сумма =", total)

    elif choice == "12":
        # For12. Произведение 1.1 * 1.2 * 1.3 * ... (N сомножителей).
        n = int(input("N: "))
        product = 1.0
        for i in range(1, n + 1):
            product *= 1 + i / 10
        print("Произведение =", product)

    elif choice == "13":
        # For13. 1.1 - 1.2 + 1.3 - ... (N слагаемых, знаки чередуются).
        n = int(input("N: "))
        total = 0.0
        sign = 1
        for i in range(1, n + 1):
            total += sign * (1 + i / 10)
            sign = -sign
        print("Значение =", total)

    elif choice == "14":
        # For14. N^2 = 1 + 3 + 5 + ... + (2N - 1).
        n = int(input("N: "))
        square = 0
        for i in range(1, n + 1):
            square += 2 * i - 1
        print("N^2 =", square)

    elif choice == "15":
        # For15. A в степени N: A * A * ... * A (N раз).
        a = float(input("A: "))
        n = int(input("N: "))
        power = 1.0
        for _ in range(n):
            power *= a
        print("A^N =", power)

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
