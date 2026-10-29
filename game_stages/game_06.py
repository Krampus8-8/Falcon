# ================================================
# ИГРА «ЗАБРОШЕННАЯ ШАХТА»
# Автор: Кашулинский Лев
# Дата: сентябрь 2026
#
# Пункт 4 - «постучать по стене»: герой стучит
# по камню и по звуку ищет пустоты и тайники,
# за это прибавляется удача.
# Масло в лампе - это запас сил героя. Без света
# идти опасно: недостающее масло забирает здоровье.
# ================================================

# --- Заголовок ------------------------------------
title = "ЗАБРОШЕННАЯ ШАХТА"
frame = "=" * 23
print(frame)
print("   " + title + "   ")
print(frame)
print()

# --- Знакомство с героем --------------------------
print("Как зовут героя?")
hero_name = input()
print(f"Добро пожаловать, {hero_name}!")
print("Ты спускаешься в старую шахту. Со стен сыплется угольная пыль, где-то капает вода.")
print()

# --- Настройка героя -------------------------------
print("Настройка героя.")
print("Здоровье, сила, ловкость, удача - по одному числу в строке:")
# если хоть одно число неверное, перечитываем все четыре:
# половине набора доверять нельзя, порядок мог сбиться
while True:
    try:
        health = int(input())
        strength = int(input())
        agility = int(input())
        luck = int(input())
        if health < 10 or health > 200:
            raise ValueError(f"Здоровье должно быть от 10 до 200, а введено {health}")
        if strength < 1 or agility < 1:
            raise ValueError("Сила и ловкость должны быть не меньше 1")
        if luck < 0 or luck > 10:
            raise ValueError(f"Удача бывает от 0 до 10, а введено {luck}")
        break
    except ValueError as e:
        if "invalid literal" in str(e):
            print("Это не число. Шахтёр так не считает! Введи все четыре числа заново:")
        else:
            print(f"{e}. Введи все четыре числа заново:")

# --- Расчёт урона ----------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
# масло в лампе: сколько раз можно зажечь лампу.
# деление нацело, потому что половину раза зажечь нельзя
lamp_oil = (health + luck * 10) // 25
max_oil = lamp_oil

# --- Формуляр героя --------------------------------
print("Характеристики героя:")
print(f"Здоровье: {health}")
print(f"Сила:     {strength}")
print(f"Ловкость: {agility}")
print(f"Удача:    {luck}")
print()
print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Масло в лампе: {lamp_oil}")
print()

# --- Главный цикл игры ----------------------------
running = True
menu_last = 6
outcome = "прерывание"
actions = 0
try:
    while running:
        print("Что делаешь?")
        print("1 - осмотреться")
        print("2 - идти вперёд")
        print("3 - отдохнуть")
        print("4 - постучать по стене")
        print("5 - зажечь шахтёрскую лампу")
        print("6 - тренировка")
        print("0 - подняться на поверхность")

        # --- Проверка пункта меню ---------------------
        while True:
            choice = input()
            try:
                menu_number = int(choice)
            except ValueError:
                print("Нет такого пункта. Введи номер из меню (0-6).")
                continue
            if 0 <= menu_number <= menu_last:
                choice = str(menu_number)
                break
            print("Нет такого пункта. Введи номер из меню (0-6).")

        # --- Выбор действия ----------------------------
        match choice:
            case "1":
                print("Ты осмотрелся. Ржавые рельсы уходят в темноту, рядом стоит перевёрнутая вагонетка.")

            case "2":
                cost = 2
                if lamp_oil >= cost:
                    lamp_oil -= cost
                    print("Ты идёшь вперёд по рельсам. Под ногами хрустит уголь, лампа коптит.")
                else:
                    health -= (cost - lamp_oil) * 10
                    lamp_oil = 0
                    print("Лампа погасла. Ты идёшь на ощупь и ударяешься о балки.")

            case "3":
                # отдых даёт меньше, чем забирает дорога, и не больше полного запаса
                lamp_oil = min(lamp_oil + 1, max_oil)
                print("Ты присел на ящик из-под динамита и немного отдохнул.")

            case "4":
                luck = luck + 1
                print("Ты стучишь по стене. В одном месте звук глухой: там пустота! Удача на твоей стороне.")

            case "5":
                if lamp_oil >= 1:
                    lamp_oil -= 1
                    health = health + 5
                    print("Ты зажёг лампу ярче. Стало светло и не так страшно, ты приободрился.")
                else:
                    print("Масла не осталось, лампа не зажигается.")

            case "6":
                strikes = 6
                total_damage = 0
                crit_count = 0
                print("В тупике висит старый мешок с углём.")
                print("Шахтёры били по нему кирками, когда спорили, кто сильнее.")
                print()
                print(f"Наносишь {strikes} ударов.")
                for i in range(1, strikes + 1):
                    if i % 3 == 0:
                        hit_damage = crit_damage
                        print(f"Удар {i}: {hit_damage:.1f} - критический!")
                        crit_count += 1
                    else:
                        hit_damage = damage
                        print(f"Удар {i}: {hit_damage:.1f}")
                    total_damage += hit_damage
                # тренировка тяжелее дороги, поэтому забирает больше масла
                cost = 3
                if lamp_oil >= cost:
                    lamp_oil -= cost
                else:
                    health -= (cost - lamp_oil) * 10
                    lamp_oil = 0
                print()
                print(f"Итог: {strikes} ударов, критических ударов: {crit_count}")
                print(f"Общий урон: {total_damage:.1f}")
                print(f"Средний урон: {total_damage / strikes:.1f}")

            case "0":
                print("Ты поднимаешься по лестнице к солнцу. Шахта остаётся внизу.")
                outcome = "выход"
                running = False

        if running:
            actions += 1

        # --- Состояние героя ---------------------------
        print()
        print(f"Здоровье: {health:4d}   Масло в лампе: {lamp_oil:3d}   Удача: {luck:3d}")
        print()

        # --- Проверка гибели ---------------------------
        if health <= 0:
            print(f"{hero_name} падает в темноте. Шахта забирает ещё одного искателя.")
            outcome = "гибель"
            running = False
except KeyboardInterrupt:
    print()
    print("Игрок бросил кирку и убежал (Ctrl + C).")
finally:
    # --- Прощание ----------------------------------
    print(frame)
    if outcome == "гибель":
        print(f"Ты не выбрался, {hero_name}. Действий совершено: {actions}.")
        print("Может, в следующий раз возьмёшь больше масла.")
    elif outcome == "выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
        print("Ты снова видишь небо. Отличная работа!")
    else:
        print(f"Сеанс прерван, {hero_name}. Действий совершено: {actions}.")
        print("Шахта подождёт твоего возвращения.")
    print(frame)
