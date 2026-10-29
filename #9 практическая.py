# 9 практическая. Функции. Задачи Proc1-Proc15
import math


def power_a3(a):
    """Proc1. Третья степень числа a."""
    return a ** 3


def power_a234(a):
    """Proc2. Вторая, третья и четвёртая степени числа a."""
    return a ** 2, a ** 3, a ** 4


def mean(x, y):
    """Proc3. Среднее арифметическое и среднее геометрическое двух положительных чисел."""
    return (x + y) / 2, math.sqrt(x * y)


def triangle_ps(a):
    """Proc4. Периметр и площадь равностороннего треугольника со стороной a."""
    return 3 * a, a ** 2 * math.sqrt(3) / 4


def rect_ps(x1, y1, x2, y2):
    """Proc5. Периметр и площадь прямоугольника по противоположным вершинам."""
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return 2 * (width + height), width * height


def digit_count_sum(k):
    """Proc6. Количество цифр и сумма цифр целого положительного числа k."""
    count = 0
    total = 0
    while k > 0:
        total += k % 10
        count += 1
        k //= 10
    return count, total


def invert_digits(k):
    """Proc7. Число k с обратным порядком цифр."""
    rev = 0
    while k > 0:
        rev = rev * 10 + k % 10
        k //= 10
    return rev


def add_right_digit(d, k):
    """Proc8. Приписать к числу k справа цифру d."""
    return k * 10 + d


def add_left_digit(d, k):
    """Proc9. Приписать к числу k слева цифру d."""
    count, _ = digit_count_sum(k)
    return d * 10 ** count + k


def swap(x, y):
    """Proc10. Пара значений в обратном порядке."""
    return y, x


def minmax(x, y):
    """Proc11. Пара (меньшее, большее)."""
    if x < y:
        return x, y
    return y, x


def sort_inc3(a, b, c):
    """Proc12. Три значения по возрастанию."""
    a, b = minmax(a, b)
    b, c = minmax(b, c)
    a, b = minmax(a, b)
    return a, b, c


def sort_dec3(a, b, c):
    """Proc13. Три значения по убыванию (зеркало Proc12)."""
    low, middle, high = sort_inc3(a, b, c)
    return high, middle, low


def shift_right3(a, b, c):
    """Proc14. Правый циклический сдвиг: a на место b, b на место c, c на место a."""
    return c, a, b


def shift_left3(a, b, c):
    """Proc15. Левый циклический сдвиг: a на место c, c на место b, b на место a."""
    return b, c, a


while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 9. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("1  - Proc1  (Третья степень пяти чисел)")
    print("3  - Proc3  (Два средних для пар)")
    print("6  - Proc6  (Количество и сумма цифр)")
    print("10 - Proc10 (Обмен пар значений)")
    print("12 - Proc12 (Тройка по возрастанию)")
    print("--- Делаем сами ---")
    print("2  - Proc2  (Степени 2, 3, 4)")
    print("4  - Proc4  (Равносторонний треугольник)")
    print("5  - Proc5  (Прямоугольник по вершинам)")
    print("7  - Proc7  [HARD] (Перевернуть цифры)")
    print("8  - Proc8  (Приписать цифру справа)")
    print("9  - Proc9  (Приписать цифру слева)")
    print("11 - Proc11 [HARD] (Минимум и максимум четырёх чисел)")
    print("13 - Proc13 (Тройка по убыванию)")
    print("14 - Proc14 [HARD] (Правый циклический сдвиг)")
    print("15 - Proc15 (Левый циклический сдвиг)")
    print("0  - Выход")
    print("=" * 60)

    choice = input("Введите номер задачи: ").strip()

    if choice == "0":
        print("Программа завершена.")
        break

    elif choice == "1":
        for i in range(5):
            a = float(input(f"Число {i + 1}: "))
            print(power_a3(a))

    elif choice == "2":
        for i in range(5):
            a = float(input(f"Число {i + 1}: "))
            square, cube, fourth = power_a234(a)
            print(square)
            print(cube)
            print(fourth)

    elif choice == "3":
        a = float(input("A: "))
        b = float(input("B: "))
        c = float(input("C: "))
        d = float(input("D: "))
        for other in (b, c, d):
            arithmetic, geometric = mean(a, other)
            print(arithmetic)
            print(geometric)

    elif choice == "4":
        for i in range(3):
            side = float(input(f"Сторона {i + 1}: "))
            perimeter, area = triangle_ps(side)
            print(perimeter)
            print(area)

    elif choice == "5":
        for i in range(3):
            print(f"Прямоугольник {i + 1}:")
            x1 = float(input("x1: "))
            y1 = float(input("y1: "))
            x2 = float(input("x2: "))
            y2 = float(input("y2: "))
            perimeter, area = rect_ps(x1, y1, x2, y2)
            print(perimeter)
            print(area)

    elif choice == "6":
        for i in range(5):
            k = int(input(f"Число {i + 1}: "))
            count, total = digit_count_sum(k)
            print(count)
            print(total)

    elif choice == "7":
        for i in range(5):
            k = int(input(f"Число {i + 1}: "))
            print(invert_digits(k))

    elif choice == "8":
        k = int(input("K: "))
        d1 = int(input("D1: "))
        d2 = int(input("D2: "))
        k = add_right_digit(d1, k)
        print(k)
        k = add_right_digit(d2, k)
        print(k)

    elif choice == "9":
        k = int(input("K: "))
        d1 = int(input("D1: "))
        d2 = int(input("D2: "))
        k = add_left_digit(d1, k)
        print(k)
        k = add_left_digit(d2, k)
        print(k)

    elif choice == "10":
        a = float(input("A: "))
        b = float(input("B: "))
        c = float(input("C: "))
        d = float(input("D: "))
        a, b = swap(a, b)
        c, d = swap(c, d)
        b, c = swap(b, c)
        print(a)
        print(b)
        print(c)
        print(d)

    elif choice == "11":
        a = float(input("A: "))
        b = float(input("B: "))
        c = float(input("C: "))
        d = float(input("D: "))
        min_ab, max_ab = minmax(a, b)
        min_cd, max_cd = minmax(c, d)
        minimum, _ = minmax(min_ab, min_cd)
        _, maximum = minmax(max_ab, max_cd)
        print("Минимум:", minimum)
        print("Максимум:", maximum)

    elif choice == "12":
        for i in range(2):
            a = float(input(f"Набор {i + 1}, a: "))
            b = float(input(f"Набор {i + 1}, b: "))
            c = float(input(f"Набор {i + 1}, c: "))
            a, b, c = sort_inc3(a, b, c)
            print(a, b, c)

    elif choice == "13":
        for i in range(2):
            a = float(input(f"Набор {i + 1}, a: "))
            b = float(input(f"Набор {i + 1}, b: "))
            c = float(input(f"Набор {i + 1}, c: "))
            a, b, c = sort_dec3(a, b, c)
            print(a, b, c)

    elif choice == "14":
        for i in range(2):
            a = float(input(f"Набор {i + 1}, a: "))
            b = float(input(f"Набор {i + 1}, b: "))
            c = float(input(f"Набор {i + 1}, c: "))
            a, b, c = shift_right3(a, b, c)
            print(a, b, c)

    elif choice == "15":
        for i in range(2):
            a = float(input(f"Набор {i + 1}, a: "))
            b = float(input(f"Набор {i + 1}, b: "))
            c = float(input(f"Набор {i + 1}, c: "))
            a, b, c = shift_left3(a, b, c)
            print(a, b, c)

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
