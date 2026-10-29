# 3 практическая. Логика и ветвление. Задачи Boolean1-Boolean15, If1-If5

while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 3. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("1  - Boolean1  (A положительное)")
    print("6  - Boolean6  (A < B < C)")
    print("12 - Boolean12 (Каждое из A, B, C положительное)")
    print("14 - Boolean14 (Ровно одно из A, B, C положительное)")
    print("--- Делаем сами ---")
    print("2  - Boolean2  (A нечётное)")
    print("3  - Boolean3  (A чётное)")
    print("4  - Boolean4  (A > 2 и B <= 3)")
    print("5  - Boolean5  (A >= 0 или B < -2)")
    print("7  - Boolean7  (B между A и C)")
    print("8  - Boolean8  (Каждое из A и B нечётное)")
    print("9  - Boolean9  (Хотя бы одно из A и B нечётное)")
    print("10 - Boolean10 (Ровно одно из A и B нечётное)")
    print("11 - Boolean11 (A и B одинаковой чётности)")
    print("13 - Boolean13 (Хотя бы одно из A, B, C положительное)")
    print("15 - Boolean15 [СЛОЖНОЕ] (Ровно два из A, B, C положительные)")
    print("0  - Выход")
    print("=" * 60)

    choice = input("Введите номер задачи: ").strip()

    if choice == "0":
        print("Программа завершена.")
        break

    elif choice == "1":
        # Boolean1. «Число A является положительным».
        a = int(input("A: "))
        print(a > 0)

    elif choice == "2":
        # Boolean2. «Число A является нечетным».
        a = int(input("A: "))
        print(a % 2 != 0)

    elif choice == "3":
        # Boolean3. «Число A является четным».
        a = int(input("A: "))
        print(a % 2 == 0)

    elif choice == "4":
        # Boolean4. «Справедливы неравенства A > 2 и B <= 3».
        a = int(input("A: "))
        b = int(input("B: "))
        print(a > 2 and b <= 3)

    elif choice == "5":
        # Boolean5. «Справедливы неравенства A >= 0 или B < -2».
        a = int(input("A: "))
        b = int(input("B: "))
        print(a >= 0 or b < -2)

    elif choice == "6":
        # Boolean6. «Справедливо двойное неравенство A < B < C».
        a = int(input("A: "))
        b = int(input("B: "))
        c = int(input("C: "))
        print(a < b < c)

    elif choice == "7":
        # Boolean7. «Число B находится между числами A и C» (строго, порядок A и C любой).
        a = int(input("A: "))
        b = int(input("B: "))
        c = int(input("C: "))
        print(a < b < c or c < b < a)

    elif choice == "8":
        # Boolean8. «Каждое из чисел A и B нечетное».
        a = int(input("A: "))
        b = int(input("B: "))
        print(a % 2 != 0 and b % 2 != 0)

    elif choice == "9":
        # Boolean9. «Хотя бы одно из чисел A и B нечетное».
        a = int(input("A: "))
        b = int(input("B: "))
        print(a % 2 != 0 or b % 2 != 0)

    elif choice == "10":
        # Boolean10. «Ровно одно из чисел A и B нечетное».
        a = int(input("A: "))
        b = int(input("B: "))
        odd_count = (a % 2 != 0) + (b % 2 != 0)
        print(odd_count == 1)

    elif choice == "11":
        # Boolean11. «Числа A и B имеют одинаковую четность».
        a = int(input("A: "))
        b = int(input("B: "))
        print(a % 2 == b % 2)

    elif choice == "12":
        # Boolean12. «Каждое из чисел A, B, C положительное».
        a = int(input("A: "))
        b = int(input("B: "))
        c = int(input("C: "))
        print(a > 0 and b > 0 and c > 0)

    elif choice == "13":
        # Boolean13. «Хотя бы одно из чисел A, B, C положительное».
        a = int(input("A: "))
        b = int(input("B: "))
        c = int(input("C: "))
        print(a > 0 or b > 0 or c > 0)

    elif choice == "14":
        # Boolean14. «Ровно одно из чисел A, B, C положительное».
        a = int(input("A: "))
        b = int(input("B: "))
        c = int(input("C: "))
        positive_count = (a > 0) + (b > 0) + (c > 0)
        print(positive_count == 1)

    elif choice == "15":
        # Boolean15. «Ровно два из чисел A, B, C являются положительными».
        a = int(input("A: "))
        b = int(input("B: "))
        c = int(input("C: "))
        positive_count = (a > 0) + (b > 0) + (c > 0)
        print(positive_count == 2)

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
