# 4 практическая python4

print("--- For1: Вывод числа K ровно N раз ---")
K = int(input("Введите целое число K: "))
N = int(input("Введите количество повторений N (>0): "))

for _ in range(N): 
    print(K, end=" ")
print("\n")


print("--- For2: Числа от A до B включительно ---")
A = int(input("Введите A: "))
B = int(input("Введите B (B > A): "))

count = 0 
for num in range(A, B + 1): 
    print(num, end=" ")
    count += 1

print(f"\nКоличество выведенных чисел: {count}\n")

print("--- For3: Числа между A и B в порядке убывания (исключая границы) ---")
A = int(input("Введите A: "))
B = int(input("Введите B (B > A): "))

count = 0
for num in range(B - 1, A, -1):
    print(num, end=" ")
    count += 1

print(f"\nКоличество выведенных чисел: {count}\n")


print("--- For4: Стоимость конфет от 1 до 10 кг ---")
price_per_kg = float(input("Введите цену за 1 кг конфет: "))

for kg in range(1, 11): 
    cost = kg * price_per_kg
    print(f"{kg} кг = {cost:.2f}")
print()


print("--- For5: Стоимость конфет от 0.1 до 1.0 кг (дробный шаг) ---")
price_per_kg = float(input("Введите цену за 1 кг конфет: "))

for i in range(1, 11):
    weight = i / 10
    cost = weight * price_per_kg
    print(f"{weight:.1f} кг = {cost:.2f}")
print()

print("--- For6: Стоимость конфет от 1.2 до 2.0 кг (шаг 0.2) ---")
price_per_kg = float(input("Введите цену за 1 кг конфет: "))

for i in range(12, 21, 2):
    weight = i / 10
    cost = weight * price_per_kg
    print(f"{weight:.1f} кг = {cost:.2f}")
print()

print("--- For7: Сумма чисел от A до B ---")
A = int(input("Введите A: "))
B = int(input("Введите B (B > A): "))

total_sum = 0 
for num in range(A, B + 1):
    total_sum += num 
print(f"Сумма чисел от {A} до {B} равна: {total_sum}\n") 


print("--- For8: Произведение чисел от A до B ---")
A = int(input("Введите A: "))
B = int(input("Введите B (B > A): "))

total_product = 1 
for num in range(A, B + 1):
    total_product *= num
print(f"Произведение чисел от {A} до {B} равно: {total_product}\n")
