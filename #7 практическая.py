#7 практическая
import random

while True:
    print("\n" + "="*60)
    print("ВЫБЕРИТЕ НОМЕР ЗАДАЧИ ДЛЯ ПРОВЕРКИ (СПИСКИ):")
    print("1  - List1 (Список степеней двойки от 1 до N)")
    print("2  - List2 (Список нечетных чисел: 1, 3, 5...)")
    print("4  - List4 (Вывод элементов списка с четными индексами)")
    print("5  - List5 (Вывод элементов с нечетными индексами в обратном порядке)")
    print("6  - List6 (Вывод элементов: сначала с четными, затем с нечетными индексами)")
    print("8  - List8 (Количество элементов, больших своих левых соседей)")
    print("9  - List9 (Номер последнего максимального элемента)")
    print("10 - List10 (Поменять местами минимальный и максимальный элементы)")
    print("12 - List12 (Циклический сдвиг элементов списка вправо)")
    print("14 - List14 (Удалить из списка все элементы с четными индексами)")
    print("0  - Выход из программы")
    print("="*60)
    
    choice = input("Введите номер задания: ").strip()
    
    if choice == "0":
        print("Программа завершена. Работа со списками освоена отлично!")
        break
        
    elif choice == "1":
        print("\n--- Выполняется задание List1 ---")
        n = int(input("Введите размер списка N (> 0): "))
        powers = []
        for i in range(1, n + 1):
            powers.append(2 ** i)
        print("Сформированный список:", powers)
        
    elif choice == "2":
        print("\n--- Выполняется задание List2 ---")
        n = int(input("Введите размер списка N (> 0): "))
        odds = []
        current = 1
        while len(odds) < n:
            odds.append(current)
            current += 2
        print("Список нечетных чисел:", odds)
        
    elif choice == "4":
        print("\n--- Выполняется задание List4 ---")
        n = int(input("Введите размер тестового списка: "))
        numbers = [random.randint(10, 99) for _ in range(n)]
        print("Исходный список (индексы от 0):", numbers)
        
        print("Элементы с четными индексами:")
        for i in range(0, len(numbers), 2):
            print(f"Индекс {i}: {numbers[i]}")
            
    elif choice == "5":
        print("\n--- Выполняется задание List5 ---")
        n = int(input("Введите размер тестового списка: "))
        numbers = [random.randint(10, 99) for _ in range(n)]
        print("Исходный список:", numbers)
        
        start_index = len(numbers) - 1
        if start_index % 2 == 0:
            start_index -= 1
            
        print("Нечетные индексы в обратном порядке:")
        for i in range(start_index, -1, -2):
            print(f"Индекс {i}: {numbers[i]}")
            
    elif choice == "6":
        print("\n--- Выполняется задание List6 ---")
        n = int(input("Введите размер тестового списка: "))
        numbers = [random.randint(10, 99) for _ in range(n)]
        print("Исходный список:", numbers)
        
        print("Сначала четные индексы:")
        for i in range(0, len(numbers), 2):
            print(numbers[i], end=" ")
        print("\nЗатем нечетные индексы:")
        for i in range(1, len(numbers), 2):
            print(numbers[i], end=" ")
        print()
        
    elif choice == "8":
        print("\n--- Выполняется задание List8 ---")
        n = int(input("Введите размер тестового списка: "))
        numbers = [random.randint(10, 99) for _ in range(n)]
        print("Исходный список:", numbers)
        
        count = 0
        for i in range(1, len(numbers)):
            if numbers[i] > numbers[i - 1]:
                count += 1
        print(f"Количество элементов, больших левого соседа: {count}")
        
    elif choice == "9":
        print("\n--- Выполняется задание List9 ---")
        n = int(input("Введите размер тестового списка: "))
        numbers = [random.randint(1, 5) for _ in range(n)]  
        print("Исходный список:", numbers)
        
        max_value = numbers[0]
        max_index = 0
        
        for i in range(1, len(numbers)):
            if numbers[i] >= max_value:
                max_value = numbers[i]
                max_index = i
                
        print(f"Максимальное значение: {max_value}, его последний индекс: {max_index}")
        
    elif choice == "10":
        print("\n--- Выполняется задание List10 ---")
        n = int(input("Введите размер тестового списка: "))
        numbers = [random.randint(10, 99) for _ in range(n)]
        print("До перестановки:", numbers)
        
        min_idx = numbers.index(min(numbers))
        max_idx = numbers.index(max(numbers))
        
        numbers[min_idx], numbers[max_idx] = numbers[max_idx], numbers[min_idx]
        print("После перестановки:", numbers)
        
    elif choice == "12":
        print("\n--- Выполняется задание List12 ---")
        n = int(input("Введите размер тестового списка: "))
        numbers = [random.randint(10, 99) for _ in range(n)]
        print("До сдвига:   ", numbers)
        
        if len(numbers) > 1:
            last_element = numbers.pop()  
            numbers.insert(0, last_element)  
            
        print("После сдвига:", numbers)
        
    elif choice == "14":
        print("\n--- Выполняется задание List14 ---")
        n = int(input("Введите размер тестового списка: "))
        numbers = [random.randint(10, 99) for _ in range(n)]
        print("Исходный список:       ", numbers)
        
        start_del = len(numbers) - 1
        if start_del % 2 != 0:
            start_del -= 1
            
        for i in range(start_del, -1, -2):
            del numbers[i]
            
        print("После удаления четных индексов:", numbers)
        
    else:
        print("Неверный ввод! Пожалуйста, выберите номер из списка.")
        
    input("\nНажмите Enter для возврата в меню...")
