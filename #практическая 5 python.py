#практическая 5 python

while True:
    print("\n" + "="*40)
    print("Выберите номер задачи для проверки:")
    print("2  - Задача While2 (Количество отрезков B в A)")
    print("4  - Задача While4 (Проверка степени 3)")
    print("5  - Задача While5 (Показатель степени 2)")
    print("6  - Задача While6 (Двойной факториал N!!)")
    print("7  - Задача While7 (Наименьшее K: K² > N)")
    print("9  - Задача While9 (Наименьшее K: 3^K > N)")
    print("10 - Задача While10 (Наибольшее K: 3^K < N)")
    print("12 - Задача While12 (Макс. K для суммы 1+...+K <= N)")
    print("13 - Задача While13 (Мин. K для суммы 1+1/2+...+1/K > A)")
    print("14 - Задача While14 (Макс. K для суммы 1+1/2+...+1/K < A)")
    print("0  - Выход из программы")
    print("="*40)
    
    choice = input("Введите номер задачи: ").strip()
    
    if choice == "0":
        print("Программа завершена. Отличная работа!")
        break
        
    elif choice == "2":
        print("\n--- Выполняется задание While2 ---")
        a = float(input("Введите положительное число A: "))
        b = float(input("Введите положительное число B (A > B): "))
        free_space = a
        count = 0
        while free_space >= b:
            free_space -= b
            count += 1
        print(f"Количество отрезков B, поместившихся в A: {count}")
        
    elif choice == "4":
        print("\n--- Выполняется задание While4 ---")
        n = int(input("Введите целое число N (> 0): "))
        rest = n
        while rest % 3 == 0:
            rest = rest // 3
        print(f"Является ли степенью числа 3?: {rest == 1}")
        
    elif choice == "5":
        print("\n--- Выполняется задание While5 ---")
        n = int(input("Введите число N (степень двойки, N = 2^K): "))
        rest = n
        k = 0
        while rest > 1:
            rest = rest // 2
            k += 1
        print(f"Показатель степени K = {k}")
        
    elif choice == "6":
        print("\n--- Выполняется задание While6 ---")
        n = int(input("Введите целое число N (> 0): "))
        factorial = 1.0
        current = n
        while current > 0:
            factorial *= current
            current -= 2
        print(f"Двойной факториал N!! = {factorial}")
        
    elif choice == "7":
        print("\n--- Выполняется задание While7 ---")
        n = int(input("Введите целое число N (> 0): "))
        k = 1
        while k * k <= n:
            k += 1
        print(f"Наименьшее целое K, при котором K² > N: {k}")
        
    elif choice == "9":
        print("\n--- Выполняется задание While9 ---")
        n = int(input("Введите целое число N (> 1): "))
        power = 1
        k = 0
        while power <= n:
            power *= 3
            k += 1
        print(f"Наименьшее целое K, при котором 3^K > N: {k}")
        
    elif choice == "10":
        print("\n--- Выполняется задание While10 ---")
        n = int(input("Введите целое число N (> 1): "))
        power = 1
        k = 0
        while power * 3 < n:
            power *= 3
            k += 1
        print(f"Наибольшее целое K, при котором 3^K < N: {k}")
        
    elif choice == "12":
        print("\n--- Выполняется задание While12 ---")
        n = int(input("Введите целое число N (> 1): "))
        total_sum = 0
        k = 0
        while total_sum + (k + 1) <= n:
            k += 1
            total_sum += k
        print(f"Наибольшее целое K: {k}")
        print(f"Сумма равна: {total_sum}")
        
    elif choice == "13":
        print("\n--- Выполняется задание While13 ---")
        a = float(input("Введите число A (> 1): "))
        total_sum = 0.0
        k = 0
        while total_sum <= a:
            k += 1
            total_sum += 1 / k
        print(f"Наименьшее целое K: {k}")
        print(f"Сумма равна: {total_sum}")
        
    elif choice == "14":
        print("\n--- Выполняется задание White14 ---")
        a = float(input("Введите число A (> 1): "))
        total_sum = 0.0
        k = 0
        while total_sum + (1 / (k + 1)) < a:
            k += 1
            total_sum += 1 / k
        print(f"Наибольшее целое K: {k}")
        print(f"Сумма равна: {total_sum}")
        
    else:
        print("Неверный ввод! Пожалуйста, выберите номер из списка.")
        
    input("\nНажмите Enter, чтобы вернуться в меню...")
