# 3 практическая. Логика и ветвление. Задачи Boolean1-Boolean15, If1-If5

while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 3. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("1  - Boolean1  (A положительное)")
    print("--- Делаем сами ---")
    print("2  - Boolean2  (A нечётное)")
    print("3  - Boolean3  (A чётное)")
    print("4  - Boolean4  (A > 2 и B <= 3)")
    print("5  - Boolean5  (A >= 0 или B < -2)")
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

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
