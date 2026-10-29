# 15 практическая. Файлы и JSON. Задачи File1-File10
import os


def read_ints(name):
    """Возвращает список целых чисел из файла name (одно число в строке)."""
    with open(name, encoding="utf-8") as f:
        return [int(line) for line in f if line.strip()]


def write_ints(name, numbers):
    """Записывает числа в файл name, каждое с новой строки."""
    with open(name, "w", encoding="utf-8") as f:
        for x in numbers:
            f.write(str(x) + "\n")


while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 15. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("2  - File2  (Записать N первых чётных чисел)")
    print("5  - File5  (Количество элементов файла)")
    print("6  - File6  (K-й элемент файла)")
    print("7  - File7  (Первый, второй, предпоследний, последний)")
    print("10 - File10 (Новый файл в обратном порядке)")
    print("--- Делаем сами ---")
    print("1  - File1  [СЛОЖНОЕ] (Допустимое ли имя файла)")
    print("3  - File3  (10 членов арифметической прогрессии)")
    print("4  - File4  (Сколько из четырёх файлов существует)")
    print("8  - File8  (Первый и последний элемент в новый файл)")
    print("9  - File9  [СЛОЖНОЕ] (Конечный и начальный элемент в отсутствующий файл)")
    print("0  - Выход")
    print("=" * 60)

    choice = input("Введите номер задачи: ").strip()

    if choice == "0":
        print("Программа завершена.")
        break

    elif choice == "1":
        # File1. Если S - допустимое имя файла, создать пустой файл и вывести True.
        s = input("Имя файла S: ")
        try:
            with open(s, "w", encoding="utf-8"):
                pass
            print(True)
        except OSError:
            print(False)

    elif choice == "2":
        # File2. Записать в файл N первых положительных чётных чисел.
        name = input("Имя файла: ")
        n = int(input("N (> 1): "))
        write_ints(name, [2 * i for i in range(1, n + 1)])
        print(f"Файл {name} записан.")

    elif choice == "3":
        # File3. Записать 10 первых членов прогрессии A, A+D, A+2D, ...
        name = input("Имя файла: ")
        a = float(input("A: "))
        d = float(input("D: "))
        with open(name, "w", encoding="utf-8") as f:
            for i in range(10):
                f.write(str(a + i * d) + "\n")
        print(f"Файл {name} записан.")

    elif choice == "4":
        # File4. Сколько из четырёх файлов существует.
        count = 0
        for i in range(4):
            if os.path.exists(input(f"Имя файла {i + 1}: ")):
                count += 1
        print(count)

    elif choice == "5":
        # File5. Количество элементов файла, -1 если файла нет.
        name = input("Имя файла: ")
        if not os.path.exists(name):
            print(-1)
        else:
            count = 0
            with open(name, encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        count += 1
            print(count)

    elif choice == "6":
        # File6. K-й элемент файла (с 1), -1 если его нет.
        name = input("Имя файла: ")
        k = int(input("K: "))
        nums = read_ints(name)
        if 1 <= k <= len(nums):
            print(nums[k - 1])
        else:
            print(-1)

    elif choice == "7":
        # File7. Первый, второй, предпоследний и последний элементы.
        name = input("Имя файла (не меньше 4 чисел): ")
        nums = read_ints(name)
        print(nums[0], nums[1], nums[-2], nums[-1])

    elif choice == "8":
        # File8. Первый и последний элементы первого файла записать во второй.
        first = input("Существующий файл: ")
        second = input("Новый файл: ")
        nums = read_ints(first)
        write_ints(second, [nums[0], nums[-1]])
        print(f"Файл {second} создан.")

    elif choice == "9":
        # File9. Один файл есть, другого нет. В отсутствующий записать конечный и начальный.
        name1 = input("Имя первого файла: ")
        name2 = input("Имя второго файла: ")
        if os.path.exists(name1):
            source, target = name1, name2
        else:
            source, target = name2, name1
        nums = read_ints(source)
        write_ints(target, [nums[-1], nums[0]])
        print(f"Файл {target} создан из {source}.")

    elif choice == "10":
        # File10. Новый файл с элементами в обратном порядке.
        name = input("Исходный файл: ")
        new_name = input("Новый файл: ")
        nums = read_ints(name)
        write_ints(new_name, nums[::-1])
        print(f"Файл {new_name} записан.")

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
