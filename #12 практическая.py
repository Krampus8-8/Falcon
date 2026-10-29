# 12 практическая. Строки глубже. Задачи String1-String15

while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 12. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("1  - String1  (Код символа)")
    print("6  - String6  (Цифра, латинская или русская буква)")
    print("10 - String10 (Строка наоборот)")
    print("--- Делаем сами ---")
    print("2  - String2  (Символ по коду)")
    print("3  - String3  (Соседи символа в таблице)")
    print("4  - String4  (N первых заглавных латинских букв)")
    print("5  - String5  [СЛОЖНОЕ] (N последних строчных букв от z)")
    print("7  - String7  (Коды первого и последнего символа)")
    print("8  - String8  (Строка из N символов C)")
    print("9  - String9  [СЛОЖНОЕ] (Чередование C1 и C2)")
    print("0  - Выход")
    print("=" * 60)

    choice = input("Введите номер задачи: ").strip()

    if choice == "0":
        print("Программа завершена.")
        break

    elif choice == "1":
        # String1. Код символа C.
        c = input("Символ C: ")
        print(ord(c))

    elif choice == "2":
        # String2. Символ с кодом N (32 <= N <= 126).
        n = int(input("Код N: "))
        print(chr(n))

    elif choice == "3":
        # String3. Символ перед C и после C в кодовой таблице.
        c = input("Символ C: ")
        print(chr(ord(c) - 1), chr(ord(c) + 1))

    elif choice == "4":
        # String4. Строка из N первых заглавных латинских букв.
        n = int(input("N (1-26): "))
        print("".join(chr(ord("A") + i) for i in range(n)))

    elif choice == "5":
        # String5. N последних строчных латинских букв в обратном порядке, начиная с z.
        n = int(input("N (1-26): "))
        print("".join(chr(ord("z") - i) for i in range(n)))

    elif choice == "6":
        # String6. digit, lat или rus.
        c = input("Символ C: ")
        if "0" <= c <= "9":
            print("digit")
        elif "a" <= c.lower() <= "z":
            print("lat")
        else:
            print("rus")

    elif choice == "7":
        # String7. Коды первого и последнего символа.
        s = input("Строка: ")
        print(ord(s[0]), ord(s[-1]))

    elif choice == "8":
        # String8. Строка длины N из символов C.
        n = int(input("N: "))
        c = input("Символ C: ")
        print(c * n)

    elif choice == "9":
        # String9. Строка длины N из чередующихся C1 и C2, начиная с C1.
        n = int(input("Чётное N: "))
        c1 = input("C1: ")
        c2 = input("C2: ")
        print("".join(c1 if i % 2 == 0 else c2 for i in range(n)))

    elif choice == "10":
        # String10. Строка в обратном порядке.
        s = input("Строка: ")
        print(s[::-1])

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
