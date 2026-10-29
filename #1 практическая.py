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
    print("6  - Begin6  (Объём и площадь параллелепипеда)")
    print("7  - Begin7  (Длина окружности и площадь круга)")
    print("8  - Begin8  (Среднее арифметическое)")
    print("9  - Begin9  [СЛОЖНОЕ] (Среднее геометрическое)")
    print("10 - Begin10 (Действия с квадратами чисел)")
    print("11 - Begin11 (Действия с модулями чисел)")
    print("12 - Begin12 [СЛОЖНОЕ] (Гипотенуза и периметр)")
    print("13 - Begin13 [СЛОЖНОЕ] (Площадь кольца)")
    print("14 - Begin14 [СЛОЖНОЕ] (Радиус и площадь по длине окружности)")
    print("15 - Begin15 [СЛОЖНОЕ] (Диаметр и длина окружности по площади)")
    print("16 - Begin16 (Расстояние между точками на оси)")
    print("17 - Begin17 (Отрезки AC, BC и их сумма)")
    print("18 - Begin18 [СЛОЖНОЕ] (Произведение отрезков AC и BC)")
    print("19 - Begin19 [СЛОЖНОЕ] (Периметр и площадь прямоугольника по вершинам)")
    print("20 - Begin20 [СЛОЖНОЕ] (Расстояние между точками на плоскости)")
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

    elif choice == "6":
        # Begin6. Даны ребра a, b, c параллелепипеда. V = a·b·c, S = 2·(a·b + b·c + a·c).
        a = float(input("Ребро a: "))
        b = float(input("Ребро b: "))
        c = float(input("Ребро c: "))
        volume = a * b * c
        surface = 2 * (a * b + b * c + a * c)
        print("Объём V =", volume)
        print("Площадь поверхности S =", surface)

    elif choice == "7":
        # Begin7. Найти длину окружности L = 2·π·R и площадь круга S = π·R².
        radius = float(input("Радиус R: "))
        length = 2 * PI * radius
        area = PI * radius ** 2
        print("Длина окружности L =", length)
        print("Площадь круга S =", area)

    elif choice == "8":
        # Begin8. Даны два числа a и b. Найти их среднее арифметическое.
        a = float(input("Число a: "))
        b = float(input("Число b: "))
        average = (a + b) / 2
        print("Среднее арифметическое =", average)

    elif choice == "9":
        # Begin9. Даны два неотрицательных числа. Найти среднее геометрическое √(a·b).
        a = float(input("Число a (>= 0): "))
        b = float(input("Число b (>= 0): "))
        geometric = math.sqrt(a * b)
        print("Среднее геометрическое =", geometric)

    elif choice == "10":
        # Begin10. Сумма, разность, произведение и частное квадратов двух ненулевых чисел.
        a = float(input("Число a (не 0): "))
        b = float(input("Число b (не 0): "))
        sq_a = a ** 2
        sq_b = b ** 2
        print("Сумма квадратов:", sq_a + sq_b)
        print("Разность квадратов:", sq_a - sq_b)
        print("Произведение квадратов:", sq_a * sq_b)
        print("Частное квадратов:", sq_a / sq_b)

    elif choice == "11":
        # Begin11. Сумма, разность, произведение и частное модулей двух ненулевых чисел.
        a = float(input("Число a (не 0): "))
        b = float(input("Число b (не 0): "))
        abs_a = abs(a)
        abs_b = abs(b)
        print("Сумма модулей:", abs_a + abs_b)
        print("Разность модулей:", abs_a - abs_b)
        print("Произведение модулей:", abs_a * abs_b)
        print("Частное модулей:", abs_a / abs_b)

    elif choice == "12":
        # Begin12. Катеты a и b. Гипотенуза c = √(a² + b²), периметр P = a + b + c.
        a = float(input("Катет a: "))
        b = float(input("Катет b: "))
        hypotenuse = math.sqrt(a ** 2 + b ** 2)
        perimeter = a + b + hypotenuse
        print("Гипотенуза c =", hypotenuse)
        print("Периметр P =", perimeter)

    elif choice == "13":
        # Begin13. Радиусы R1 > R2. S1 = π·R1², S2 = π·R2², S3 = S1 - S2 (кольцо).
        r1 = float(input("Внешний радиус R1: "))
        r2 = float(input("Внутренний радиус R2 (меньше R1): "))
        s1 = PI * r1 ** 2
        s2 = PI * r2 ** 2
        s3 = s1 - s2
        print("S1 =", s1)
        print("S2 =", s2)
        print("Площадь кольца S3 =", s3)

    elif choice == "14":
        # Begin14. Дана длина окружности L. Найти радиус R = L / (2·π) и площадь S = π·R².
        length = float(input("Длина окружности L: "))
        radius = length / (2 * PI)
        area = PI * radius ** 2
        print("Радиус R =", radius)
        print("Площадь S =", area)

    elif choice == "15":
        # Begin15. Дана площадь круга S. Найти диаметр D и длину окружности L.
        area = float(input("Площадь круга S: "))
        radius = math.sqrt(area / PI)
        diameter = 2 * radius
        length = 2 * PI * radius
        print("Диаметр D =", diameter)
        print("Длина окружности L =", length)

    elif choice == "16":
        # Begin16. Расстояние между точками x1 и x2 на числовой оси: |x2 - x1|.
        x1 = float(input("x1: "))
        x2 = float(input("x2: "))
        distance = abs(x2 - x1)
        print("Расстояние =", distance)

    elif choice == "17":
        # Begin17. Точки A, B, C на оси. Найти длины AC, BC и их сумму.
        a = float(input("Точка A: "))
        b = float(input("Точка B: "))
        c = float(input("Точка C: "))
        ac = abs(c - a)
        bc = abs(c - b)
        print("AC =", ac)
        print("BC =", bc)
        print("Сумма AC + BC =", ac + bc)

    elif choice == "18":
        # Begin18. Точка C между A и B. Найти произведение длин AC и BC.
        a = float(input("Точка A: "))
        b = float(input("Точка B: "))
        c = float(input("Точка C (между A и B): "))
        ac = abs(c - a)
        bc = abs(b - c)
        print("AC * BC =", ac * bc)

    elif choice == "19":
        # Begin19. Противоположные вершины (x1, y1) и (x2, y2). Найти периметр и площадь.
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        print("Периметр =", 2 * (width + height))
        print("Площадь =", width * height)

    elif choice == "20":
        # Begin20. Расстояние между (x1, y1) и (x2, y2): √((x2 - x1)² + (y2 - y1)²).
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print("Расстояние =", distance)

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
