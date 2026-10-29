# 4 практическая. Циклы for. Задачи For1-For15

while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 4. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("1  - For1  (Вывести N раз число K)")
    print("3  - For3  (Числа между A и B по убыванию)")
    print("--- Делаем сами ---")
    print("2  - For2  (Числа от A до B по возрастанию и их количество)")
    print("4  - For4  (Стоимость 1..10 кг конфет)")
    print("5  - For5  [СЛОЖНОЕ] (Стоимость 0.1..1 кг)")
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

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
