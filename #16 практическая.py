# 16 практическая (занятия 16-17). Классы. Задачи Class1-Class8


class Point:
    """Точка на плоскости с координатами x и y."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def shift(self, dx, dy):
        """Class2. Сдвигает точку на dx и dy. Возвращает None."""
        self.x += dx
        self.y += dy

    def __str__(self):
        """Class7. Строка вида (x, y)."""
        return f"({self.x}, {self.y})"


class Counter:
    """Class3. Счётчик, который начинается с нуля."""

    def __init__(self):
        self.total = 0

    def inc(self):
        self.total += 1

    def dec(self):
        self.total -= 1

    def value(self):
        return self.total


class Potion:
    """Class4. Зелье с названием, ценой и силой лечения."""

    def __init__(self, name, price, heal):
        self.name = name
        self.price = price
        self.heal = heal

    def describe(self):
        return f"{self.name}: {self.price} gold, +{self.heal} health"


class Inventory:
    """Class6. Инвентарь: словарь предмет -> количество."""

    def __init__(self):
        self.items = {}

    def add(self, name, qty):
        self.items[name] = self.items.get(name, 0) + qty

    def total(self):
        return sum(self.items.values())


class Hero:
    """Class8. Герой с именем, здоровьем и уроном, умеет сохраняться в словарь."""

    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def to_dict(self):
        return {"name": self.name, "health": self.health, "damage": self.damage}

    @staticmethod
    def from_dict(data):
        return Hero(data["name"], data["health"], data["damage"])


def read_point():
    x = int(input("x: "))
    y = int(input("y: "))
    return Point(x, y)


while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 16-17. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("1  - Class1 (Класс Point)")
    print("3  - Class3 (Класс Counter)")
    print("--- Делаем сами ---")
    print("2  - Class2 (Метод shift)")
    print("4  - Class4 (Класс Potion и describe)")
    print("0  - Выход")
    print("=" * 60)

    choice = input("Введите номер задачи: ").strip()

    if choice == "0":
        print("Программа завершена.")
        break

    elif choice == "1":
        p = read_point()
        print(p.x)
        print(p.y)

    elif choice == "2":
        p = read_point()
        dx = int(input("dx: "))
        dy = int(input("dy: "))
        p.shift(dx, dy)
        print(p.x)
        print(p.y)

    elif choice == "3":
        c = Counter()
        for i in range(3):
            cmd = input("Команда (inc, dec, value): ").strip()
            if cmd == "inc":
                c.inc()
            elif cmd == "dec":
                c.dec()
            else:
                print(c.value())

    elif choice == "4":
        name = input("Название: ")
        price = int(input("Цена: "))
        heal = int(input("Лечение: "))
        potion = Potion(name, price, heal)
        print(potion.describe())

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
