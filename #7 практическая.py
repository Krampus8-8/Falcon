# 7 практическая. Списки и random. Задачи List1-List15

while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 7. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("1  - List1  (Длина и первый элемент)")
    print("4  - List4  (Максимум и его индекс)")
    print("--- Делаем сами ---")
    print("2  - List2  (A[K], последний элемент, сколько перед K)")
    print("3  - List3  (Сумма и произведение на чётных индексах)")
    print("5  - List5  (Добавить D в конец)")
    print("0  - Выход")
    print("=" * 60)

    choice = input("Введите номер задачи: ").strip()

    if choice == "0":
        print("Программа завершена.")
        break

    if choice in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "11", "12", "13", "14", "15"):
        # во всех задачах, кроме List10, сначала читаем список чисел
        n = int(input("Количество элементов N: "))
        a = []
        for i in range(n):
            a.append(int(input(f"Элемент {i + 1}: ")))

    if choice == "1":
        # List1. Вывести длину списка и первый элемент.
        print("Длина:", len(a))
        print("Первый элемент:", a[0])

    elif choice == "2":
        # List2. Вывести A[K], последний элемент и число элементов перед K.
        k = int(input("Индекс K: "))
        print("A[K] =", a[k])
        print("Последний элемент:", a[-1])
        print("Элементов перед K:", k)

    elif choice == "3":
        # List3. Сумма элементов и произведение элементов с чётными индексами.
        product = 1
        for i in range(0, len(a), 2):
            product *= a[i]
        print("Сумма:", sum(a))
        print("Произведение на чётных индексах:", product)

    elif choice == "4":
        # List4. Максимальный элемент и его индекс (сначала индекс).
        max_index = 0
        for i in range(1, len(a)):
            if a[i] > a[max_index]:
                max_index = i
        print("Индекс:", max_index)
        print("Максимум:", a[max_index])

    elif choice == "5":
        # List5. Добавить D в конец, вывести список и длину.
        d = int(input("D: "))
        a.append(d)
        print(a)
        print("Длина:", len(a))

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
