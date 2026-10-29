# Домашнее задание к занятию 10: две рекурсии и их двойники на циклах


def factorial_rec(n):
    """Факториал n! рекурсией: n! = n * (n - 1)!, база 0! = 1."""
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)


def factorial_loop(n):
    """Тот же факториал циклом for."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def digit_sum_rec(k):
    """Сумма цифр рекурсией: последняя цифра + сумма цифр без неё, база k < 10."""
    if k < 10:
        return k
    return k % 10 + digit_sum_rec(k // 10)


def digit_sum_loop(k):
    """Та же сумма цифр циклом while."""
    total = 0
    while k > 0:
        total += k % 10
        k //= 10
    return total


n = int(input("Число для факториала: "))
print("Рекурсия:", factorial_rec(n))
print("Цикл:    ", factorial_loop(n))

k = int(input("Число для суммы цифр: "))
print("Рекурсия:", digit_sum_rec(k))
print("Цикл:    ", digit_sum_loop(k))

# Сравнение: рекурсия короче и похожа на математическое определение,
# но каждый вызов занимает кадр стека, и при n около 1000 Python
# выдаст RecursionError. Цикл работает с любым n и не тратит стек.
