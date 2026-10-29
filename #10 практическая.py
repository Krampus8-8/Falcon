# 10 практическая. Функции глубже. Задачи Proc16-Proc30
import math

PI = 3.14


def sign(x):
    """Proc16. -1 при x < 0, 0 при x = 0, 1 при x > 0."""
    if x < 0:
        return -1
    if x == 0:
        return 0
    return 1


def roots_count(a, b, c):
    """Proc17. Количество корней квадратного уравнения (a != 0)."""
    d = b * b - 4 * a * c
    if abs(d) < 1e-9:
        return 1
    if d > 0:
        return 2
    return 0


def circle_s(r):
    """Proc18. Площадь круга радиуса r."""
    return PI * r ** 2


def ring_s(r1, r2):
    """Proc19. Площадь кольца между окружностями r1 > r2."""
    return circle_s(r1) - circle_s(r2)


def triangle_p(a, h):
    """Proc20. Периметр равнобедренного треугольника по основанию a и высоте h."""
    side = math.sqrt((a / 2) ** 2 + h ** 2)
    return a + 2 * side


def sum_range(a, b):
    """Proc21. Сумма целых от a до b включительно, 0 если a > b."""
    if a > b:
        return 0
    total = 0
    for x in range(a, b + 1):
        total += x
    return total


def calc(a, b, op):
    """Proc22. 1 - вычитание, 2 - умножение, 3 - деление, иначе сложение."""
    if op == 1:
        return a - b
    if op == 2:
        return a * b
    if op == 3:
        return a / b
    return a + b


def quarter(x, y):
    """Proc23. Номер координатной четверти точки (x, y) с ненулевыми координатами."""
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4


def even(k):
    """Proc24. True для чётного k."""
    return k % 2 == 0


def is_square(k):
    """Proc25. True, если k (> 0) - квадрат целого числа."""
    r = int(k ** 0.5)
    return r * r == k or (r + 1) * (r + 1) == k


def is_power_n(k, n):
    """Proc27. True, если k (> 0) - степень числа n (> 1)."""
    while k % n == 0:
        k //= n
    return k == 1


def is_power5(k):
    """Proc26. True, если k (> 0) - степень пятёрки."""
    return is_power_n(k, 5)


def is_prime(n):
    """Proc28. True, если n (> 1) простое."""
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def digit_count(k):
    """Proc29. Количество цифр числа k (> 0)."""
    count = 0
    while k > 0:
        count += 1
        k //= 10
    return count


def digit_n(k, n):
    """Proc30. n-я цифра числа k справа налево, -1 если цифр меньше n."""
    if digit_count(k) < n:
        return -1
    return k // 10 ** (n - 1) % 10


def read_ten():
    numbers = []
    for i in range(10):
        numbers.append(int(input(f"Число {i + 1}: ")))
    return numbers


while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 10. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("16 - Proc16 (Sign(A) + Sign(B))")
    print("19 - Proc19 (Площади трёх колец)")
    print("--- Делаем сами ---")
    print("17 - Proc17 (Количество корней уравнения)")
    print("18 - Proc18 (Площади трёх кругов)")
    print("20 - Proc20 [СЛОЖНОЕ] (Периметр равнобедренного треугольника)")
    print("0  - Выход")
    print("=" * 60)

    choice = input("Введите номер задачи: ").strip()

    if choice == "0":
        print("Программа завершена.")
        break

    elif choice == "16":
        a = float(input("A: "))
        b = float(input("B: "))
        print(sign(a) + sign(b))

    elif choice == "17":
        for i in range(3):
            print(f"Уравнение {i + 1}:")
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            print(roots_count(a, b, c))

    elif choice == "18":
        for i in range(3):
            r = float(input(f"Радиус {i + 1}: "))
            print(circle_s(r))

    elif choice == "19":
        for i in range(3):
            r1 = float(input(f"Кольцо {i + 1}, R1: "))
            r2 = float(input(f"Кольцо {i + 1}, R2: "))
            print(ring_s(r1, r2))

    elif choice == "20":
        for i in range(3):
            a = float(input(f"Треугольник {i + 1}, основание a: "))
            h = float(input(f"Треугольник {i + 1}, высота h: "))
            print(triangle_p(a, h))

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
