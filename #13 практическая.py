# 13 практическая. Кортежи, множества и двумерные структуры. Задачи Matrix1-Matrix10


def read_matrix():
    """Читает M, N и M строк по N чисел через пробел. Возвращает (m, n, матрица)."""
    m = int(input("M (строк): "))
    n = int(input("N (столбцов): "))
    matrix = []
    for i in range(m):
        row = [int(x) for x in input(f"Строка {i + 1} ({n} чисел через пробел): ").split()]
        matrix.append(row)
    return m, n, matrix


def read_values(count):
    """Читает набор из count чисел через пробел."""
    return [int(x) for x in input(f"Набор из {count} чисел через пробел: ").split()]


def print_matrix(matrix):
    for row in matrix:
        print(row)


while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 13. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("1  - Matrix1  (Строка I заполнена числом 10*I)")
    print("4  - Matrix4  (Каждая строка - исходный набор)")
    print("7  - Matrix7  (K-я строка матрицы)")
    print("8  - Matrix8  (K-й столбец матрицы)")
    print("9  - Matrix9  (Строки с чётными номерами)")
    print("--- Делаем сами ---")
    print("2  - Matrix2  (Столбец J заполнен числом 5*J)")
    print("3  - Matrix3  (Каждый столбец - исходный набор)")
    print("5  - Matrix5  [СЛОЖНОЕ] (Столбцы с шагом D)")
    print("6  - Matrix6  [СЛОЖНОЕ] (Строки с множителем Q)")
    print("10 - Matrix10 (Столбцы с нечётными номерами)")
    print("0  - Выход")
    print("=" * 60)

    choice = input("Введите номер задачи: ").strip()

    if choice == "0":
        print("Программа завершена.")
        break

    elif choice == "1":
        # Matrix1. Все элементы I-й строки равны 10*I.
        m = int(input("M: "))
        n = int(input("N: "))
        matrix = []
        for i in range(1, m + 1):
            matrix.append([10 * i for _ in range(n)])
        print_matrix(matrix)

    elif choice == "2":
        # Matrix2. Все элементы J-го столбца равны 5*J.
        m = int(input("M: "))
        n = int(input("N: "))
        matrix = []
        for _ in range(m):
            matrix.append([5 * j for j in range(1, n + 1)])
        print_matrix(matrix)

    elif choice == "3":
        # Matrix3. В каждом столбце набор из M чисел.
        m = int(input("M: "))
        n = int(input("N: "))
        values = read_values(m)
        matrix = []
        for i in range(m):
            matrix.append([values[i]] * n)
        print_matrix(matrix)

    elif choice == "4":
        # Matrix4. В каждой строке набор из N чисел (копия, а не та же строка).
        m = int(input("M: "))
        n = int(input("N: "))
        values = read_values(n)
        matrix = []
        for _ in range(m):
            matrix.append(values[:])
        print_matrix(matrix)

    elif choice == "5":
        # Matrix5. Первый столбец - набор, каждый следующий больше на D.
        m = int(input("M: "))
        n = int(input("N: "))
        d = int(input("D: "))
        values = read_values(m)
        matrix = []
        for i in range(m):
            matrix.append([values[i] + d * j for j in range(n)])
        print_matrix(matrix)

    elif choice == "6":
        # Matrix6. Первая строка - набор, каждая следующая умножена на Q.
        m = int(input("M: "))
        n = int(input("N: "))
        q = int(input("Q: "))
        values = read_values(n)
        matrix = []
        for i in range(m):
            matrix.append([x * q ** i for x in values])
        print_matrix(matrix)

    elif choice == "7":
        # Matrix7. Элементы K-й строки.
        m, n, matrix = read_matrix()
        k = int(input("K (номер строки): "))
        print(matrix[k - 1])

    elif choice == "8":
        # Matrix8. Элементы K-го столбца.
        m, n, matrix = read_matrix()
        k = int(input("K (номер столбца): "))
        print([row[k - 1] for row in matrix])

    elif choice == "9":
        # Matrix9. Строки с чётными номерами, без условного оператора.
        m, n, matrix = read_matrix()
        for row in matrix[1::2]:
            print(row)

    elif choice == "10":
        # Matrix10. Столбцы с нечётными номерами по столбцам, без условного оператора.
        m, n, matrix = read_matrix()
        for j in range(0, n, 2):
            for row in matrix:
                print(row[j], end=" ")
            print()

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
