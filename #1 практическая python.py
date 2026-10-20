#1 практическая python
import math

def begin6(a, b, c):
    V = a * b * c
    S = 2 * (a * b + b * c + a * c)
    return V, S

def begin7(R):
    pi = 3.14
    L = 2 * pi * R
    S = pi * (R ** 2)
    return L, S

def begin8(a, b):
    return (a + b) / 2

def begin9(a, b):
    return math.sqrt(a * b)

def begin10(a, b):
    sq_a = a ** 2
    sq_b = b ** 2
    return sq_a + sq_b, sq_a - sq_b, sq_a * sq_b, sq_a / sq_b

def begin11(a, b):
    abs_a = abs(a)
    abs_b = abs(b)
    return abs_a + abs_b, abs_a - abs_b, abs_a * abs_b, abs_a / abs_b

def begin12(a, b):
    c = math.sqrt(a**2 + b**2)
    P = a + b + c
    return c, P

def begin13(R1, R2):
    pi = 3.14
    S1 = pi * (R1 ** 2)
    S2 = pi * (R2 ** 2)
    S3 = S1 - S2
    return S1, S2, S3

def begin14(L):
    pi = 3.14
    R = L / (2 * pi)
    S = pi * (R ** 2)
    return R, S

def begin15(S):
    pi = 3.14
    R = math.sqrt(S / pi)
    D = 2 * R
    L = 2 * pi * R
    return D, L


def begin16(x1, x2):
    return abs(x2 - x1)

def begin17(A, B, C):
    AC = abs(C - A)
    BC = abs(C - B)
    total_sum = AC + BC
    return AC, BC, total_sum

def begin18(A, B, C):
    AC = abs(C - A)
    BC = abs(C - B)
    return AC * BC

def begin19(x1, y1, x2, y2):
    side_a = abs(x2 - x1)
    side_b = abs(y2 - y1)
    P = 2 * (side_a + side_b)
    S = side_a * side_b
    return P, S


if __name__ == "__main__":
    print("=== Примеры работы функций ===")
    print(f"Begin6 (a=2, b=3, c=4): Объем = {begin6(2, 3, 4)[0]}, Площадь = {begin6(2, 3, 4)[1]}")
    print(f"Begin7 (R=5): Длина = {begin7(5)[0]}, Площадь = {begin7(5)[1]}")
    print(f"Begin8 (a=4, b=6): Среднее арифм. = {begin8(4, 6)}")
    print(f"Begin9 (a=4, b=9): Среднее геом. = {begin9(4, 9)}")
    print(f"Begin10 (a=3, b=2): Квадраты (сумма, разн, произв, частн) = {begin10(3, 2)}")
    print(f"Begin11 (a=-5, b=2): Модули (сумма, разн, произв, частн) = {begin11(-5, 2)}")
    print(f"Begin12 (a=3, b=4): Гипотенуза = {begin12(3, 4)[0]}, Периметр = {begin12(3, 4)[1]}")
    print(f"Begin13 (R1=5, R2=3): S1 = {begin13(5, 3)[0]}, S2 = {begin13(5, 3)[1]}, S3 кольца = {begin13(5, 3)[2]}")
    print(f"Begin14 (L=31.4): Радиус = {begin14(31.4)[0]}, Площадь = {begin14(31.4)[1]}")
    print(f"Begin15 (S=78.5): Диаметр = {begin15(78.5)[0]}, Длина = {begin15(78.5)[1]}")
    print(f"Begin16 (x1=-2, x2=5): Расстояние = {begin16(-2, 5)}")
    print(f"Begin17 (A=1, B=10, C=4): AC = {begin17(1, 10, 4)[0]}, BC = {begin17(1, 10, 4)[1]}, Сумма = {begin17(1, 10, 4)[2]}")
    print(f"Begin18 (A=1, B=10, C=4): Произведение AC*BC = {begin18(1, 10, 4)}")
    print(f"Begin19 ((1,1) и (4,5)): Периметр = {begin19(1, 1, 4, 5)[0]}, Площадь = {begin19(1, 1, 4, 5)[1]}")
