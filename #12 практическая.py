# 12 практическая. Строки глубже. Задачи String1-String15

while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 12. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("1  - String1  (Код символа)")
    print("--- Делаем сами ---")
    print("2  - String2  (Символ по коду)")
    print("3  - String3  (Соседи символа в таблице)")
    print("4  - String4  (N первых заглавных латинских букв)")
    print("5  - String5  [СЛОЖНОЕ] (N последних строчных букв от z)")
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

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
