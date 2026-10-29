# 1 практическая. Первая программа. Задачи Begin1-Begin20
import math

PI = 3.14

while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 1. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ (1-20)")
    print("--- Разбираем вместе ---")
    print("1  - Begin1  (Периметр квадрата)")
    print("2  - Begin2  (Площадь квадрата)")
    print("3  - Begin3  (Площадь и периметр прямоугольника)")
    print("4  - Begin4  (Длина окружности по диаметру)")
    print("5  - Begin5  (Объём и площадь поверхности куба)")
    print("--- Делаем сами ---")
    print("0  - Выход")
    print("=" * 60)

    choice = input("Введите номер задачи: ").strip()

    if choice == "0":
        print("Программа завершена.")
        break

    elif choice == "1":
        # Begin1. Дана сторона квадрата a. Найти его периметр P = 4·a.
        side = float(input("Сторона квадрата a: "))
        perimeter = 4 * side
        print("Периметр P =", perimeter)

    elif choice == "2":
        # Begin2. Дана сторона квадрата a. Найти его площадь S = a².
        side = float(input("Сторона квадрата a: "))
        area = side ** 2
        print("Площадь S =", area)

    elif choice == "3":
        # Begin3. Даны стороны прямоугольника a и b. Найти S = a·b и P = 2·(a + b).
        a = float(input("Сторона a: "))
        b = float(input("Сторона b: "))
        area = a * b
        perimeter = 2 * (a + b)
        print("Площадь S =", area)
        print("Периметр P =", perimeter)

    elif choice == "4":
        # Begin4. Дан диаметр окружности d. Найти ее длину L = π·d.
        diameter = float(input("Диаметр d: "))
        length = PI * diameter
        print("Длина окружности L =", length)

    elif choice == "5":
        # Begin5. Дана длина ребра куба a. Найти V = a³ и S = 6·a².
        edge = float(input("Ребро куба a: "))
        volume = edge ** 3
        surface = 6 * edge ** 2
        print("Объём V =", volume)
        print("Площадь поверхности S =", surface)

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
