# 5 практическая. Цикл while. Задачи While1-While15

while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 5. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("1  - While1  (Незанятая часть отрезка без * и /)")
    print("3  - While3  (Частное и остаток через + и -)")
    print("8  - While8  (Наибольшее K, где K^2 <= N)")
    print("--- Делаем сами ---")
    print("2  - While2  (Сколько отрезков B на A без * и /)")
    print("4  - While4  [СЛОЖНОЕ] (N является степенью 3?)")
    print("5  - While5  (Показатель степени двойки)")
    print("6  - While6  (Двойной факториал N!!)")
    print("7  - While7  [СЛОЖНОЕ] (Наименьшее K, где K^2 > N)")
    print("9  - While9  (Наименьшее K, где 3^K > N)")
    print("10 - While10 (Наибольшее K, где 3^K < N)")
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

    elif choice == "6":
        # While6. Двойной факториал N!! = N * (N-2) * (N-4) * ...
        n = int(input("N: "))
        factorial = 1.0
        while n > 1:
            factorial *= n
            n -= 2
        print("N!! =", factorial)

    elif choice == "7":
        # While7. Наименьшее K, для которого K^2 > N.
        n = int(input("N: "))
        k = 1
        while k * k <= n:
            k += 1
        print("K =", k)

    elif choice == "8":
        # While8. Наибольшее K, для которого K^2 <= N.
        n = int(input("N: "))
        k = 1
        while (k + 1) * (k + 1) <= n:
            k += 1
        print("K =", k)

    elif choice == "9":
        # While9. Наименьшее K, для которого 3^K > N.
        n = int(input("N: "))
        k = 0
        power = 1
        while power <= n:
            power *= 3
            k += 1
        print("K =", k)

    elif choice == "10":
        # While10. Наибольшее K, для которого 3^K < N.
        n = int(input("N: "))
        k = 0
        power = 1
        while power * 3 < n:
            power *= 3
            k += 1
        print("K =", k)

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
