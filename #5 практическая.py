# 5 практическая. Цикл while. Задачи While1-While15

while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 5. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("1  - While1  (Незанятая часть отрезка без * и /)")
    print("3  - While3  (Частное и остаток через + и -)")
    print("--- Делаем сами ---")
    print("2  - While2  (Сколько отрезков B на A без * и /)")
    print("4  - While4  [СЛОЖНОЕ] (N является степенью 3?)")
    print("5  - While5  (Показатель степени двойки)")
    print("0  - Выход")
    print("=" * 60)

    choice = input("Введите номер задачи: ").strip()

    if choice == "0":
        print("Программа завершена.")
        break

    elif choice == "1":
        # While1. Длина незанятой части отрезка A без умножения и деления.
        a = float(input("A: "))
        b = float(input("B (меньше A): "))
        rest = a
        while rest >= b:
            rest -= b
        print("Незанятая часть:", rest)

    elif choice == "2":
        # While2. Количество отрезков B на отрезке A без умножения и деления.
        a = float(input("A: "))
        b = float(input("B (меньше A): "))
        rest = a
        pieces = 0
        while rest >= b:
            rest -= b
            pieces += 1
        print("Отрезков поместилось:", pieces)

    elif choice == "3":
        # While3. Частное и остаток от деления N на K только через + и -.
        n = int(input("N: "))
        k = int(input("K: "))
        quotient = 0
        rest = n
        while rest >= k:
            rest -= k
            quotient += 1
        print("Частное:", quotient)
        print("Остаток:", rest)

    elif choice == "4":
        # While4. Является ли N степенью числа 3.
        n = int(input("N: "))
        rest = n
        while rest % 3 == 0:
            rest //= 3
        print(rest == 1)

    elif choice == "5":
        # While5. N = 2^K. Найти K.
        n = int(input("N (степень двойки): "))
        k = 0
        while n > 1:
            n //= 2
            k += 1
        print("K =", k)

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
