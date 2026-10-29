# 2 практическая. Числа. Задачи Begin22-Begin36, Integer1-Integer5

PI = 3.14

while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 2. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("22 - Begin22 (Обмен значений A и B)")
    print("25 - Begin25 (Функция y = 3x^6 - 6x^2 - 7)")
    print("29 - Begin29 (Градусы в радианы)")
    print("--- Делаем сами ---")
    print("23 - Begin23 (Сдвиг A -> B -> C -> A)")
    print("24 - Begin24 (Сдвиг A -> C -> B -> A)")
    print("26 - Begin26 (Функция y = 4(x-3)^6 - 7(x-3)^3 + 2)")
    print("27 - Begin27 [СЛОЖНОЕ] (A^8 тремя умножениями)")
    print("28 - Begin28 [СЛОЖНОЕ] (A^15 пятью умножениями)")
    print("0  - Выход")
    print("=" * 60)

    choice = input("Введите номер задачи: ").strip()

    if choice == "0":
        print("Программа завершена.")
        break

    elif choice == "22":
        # Begin22. Поменять местами содержимое переменных A и B.
        a = float(input("A: "))
        b = float(input("B: "))
        temp = a
        a = b
        b = temp
        print("A =", a)
        print("B =", b)

    elif choice == "23":
        # Begin23. Переместить A в B, B в C, C в A.
        a = float(input("A: "))
        b = float(input("B: "))
        c = float(input("C: "))
        temp = c
        c = b
        b = a
        a = temp
        print("A =", a)
        print("B =", b)
        print("C =", c)

    elif choice == "24":
        # Begin24. Переместить A в C, C в B, B в A.
        a = float(input("A: "))
        b = float(input("B: "))
        c = float(input("C: "))
        temp = a
        a = b
        b = c
        c = temp
        print("A =", a)
        print("B =", b)
        print("C =", c)

    elif choice == "25":
        # Begin25. y = 3x^6 - 6x^2 - 7
        x = float(input("x: "))
        y = 3 * x ** 6 - 6 * x ** 2 - 7
        print("y =", y)

    elif choice == "26":
        # Begin26. y = 4(x-3)^6 - 7(x-3)^3 + 2
        x = float(input("x: "))
        shifted = x - 3
        y = 4 * shifted ** 6 - 7 * shifted ** 3 + 2
        print("y =", y)

    elif choice == "27":
        # Begin27. A^8 через A^2, A^4, A^8 (три умножения).
        a = float(input("A: "))
        power2 = a * a
        power4 = power2 * power2
        power8 = power4 * power4
        print("A^2 =", power2)
        print("A^4 =", power4)
        print("A^8 =", power8)

    elif choice == "28":
        # Begin28. A^15 через A^2, A^3, A^5, A^10, A^15 (пять умножений).
        a = float(input("A: "))
        power2 = a * a
        power3 = power2 * a
        power5 = power3 * power2
        power10 = power5 * power5
        power15 = power10 * power5
        print("A^2 =", power2)
        print("A^3 =", power3)
        print("A^5 =", power5)
        print("A^10 =", power10)
        print("A^15 =", power15)

    elif choice == "29":
        # Begin29. Угол в градусах (0 < a < 360) перевести в радианы.
        degrees = float(input("Угол в градусах: "))
        radians = degrees * PI / 180
        print("В радианах:", radians)

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
