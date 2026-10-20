# 3 практическая python
print("--- 1. Сравнения и логические значения ---")
x = float(input("Введите число для проверки: "))
is_positive = x > 0  
print(f"Число больше нуля? Ответ: {is_positive} (Тип: {type(is_positive)})")

print("\n--- 2. Приём подсчета истинных условий ---")
print("Введите три числа, а программа посчитает, сколько из них положительные:")
num1 = float(input("Первое число: "))
num2 = float(input("Второе число: "))
num3 = float(input("Третье число: "))

positive_count = (num1 > 0) + (num2 > 0) + (num3 > 0)
print(f"Количество положительных чисел: {positive_count}")

exact_one = positive_count == 1
print(f"Ровно одно из трёх положительное? {exact_one}")

print("\n--- 3. Цепочки сравнений ---")
age = float(input("Введите возраст: "))
if 14 <= age <= 22:
    print("Вы подходите под категорию: Юношество (от 14 до 22 лет)")
else:
    print("Вы не входите в диапазон от 14 до 22 лет")

print("\n--- 4. Проверка истинности (bool) ---")
user_input = input("Введите что-нибудь (или просто нажмите Enter для пустоты): ")

if user_input: 
    print(f"Вы ввели непустую строку! Функция bool('{user_input}') вернет True")
else:  # Если нажали просто Enter, строка пустая "" -> False
    print("Вы ничего не ввели. Пустая строка дает False")


print("\n--- 5. Полное разветвление (if-elif-else) ---")
score = float(input("Введите вашу оценку (от 1 до 5): "))

if score == 5:
    print("Отлично!")
elif score == 4:
    print("Хорошо")
elif score >= 1:
    print("Нужно подтянуть знания")
else:
    print("Такой оценки не существует")

print("\n--- 6. Разветвление через match/case ---")
action = input("Куда пойдет герой? (вперед, назад, стоять): ").strip().lower()

match action:
    case "вперед":
        print("Герой делает шаг вперед.")
    case "назад":
        print("Герой отступает.")
    case "стоять":
        print("Герой замер на месте.")
    case _:  
        print("Неизвестная команда!")
