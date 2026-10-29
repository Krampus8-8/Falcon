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
# Новая кирка из лавки даёт +2 к урону за каждую купленную штуку,
# две кирки дают +4. Бинты и масло не поднимают выше стартового запаса.
# ================================================

import random

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
max_health = health

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
# --- Враги и журнал боя ---------------------------
enemies = ["крыса-мутант", "шахтёр-призрак", "угольный голем", "летучая мышь"]
log = []
gold_total = 0
prices = {"bandage": 10, "lamp_oil": 15, "pickaxe": 40}
ability_bonus = 0


# --- Функции игры ---------------------------------
def hero_hit(strike_n):
    """Урон героя в удар номер strike_n.
    Возвращает пару (hit, crit): урон и признак критического удара.
    Читает глобальные правила damage и crit_damage, ничего не меняет.
    """
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False


def fight(enemy, hero_health, bonus=0):
    """Бой с enemy до гибели одного из двоих.
    bonus - надбавка к урону героя, по умолчанию 0. Прибавляется
    после удвоения критом, то есть крит не удваивает надбавку.
    Печатает строки раундов. Возвращает (rounds, won, hero_health, loot):
    таблицу раундов, признак победы, здоровье после боя и золото.
    Глобальные переменные не меняет.
    """
    enemy_hp = 45.0
    rounds = []
    round_n = 0
    print(f"Ты спускаешься по ржавой лестнице. Из темноты выходит {enemy}!")
    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n)
        hit = hit + bonus
        enemy_hp -= hit
        line = f"Раунд {round_n}: ты наносишь {hit:.1f}"
        if crit:
            line += " - критический!"
        if enemy_hp <= 0:
            line += " Враг падает."
            rounds.append([round_n, hit, 0])
        else:
            enemy_hit = random.randint(2, 6)
            hero_health -= enemy_hit
            line += f". У врага осталось {enemy_hp:.1f}. Ответный удар: {enemy_hit}."
            rounds.append([round_n, hit, enemy_hit])
        print(line)
    won = enemy_hp <= 0
    if won:
        loot = 10 + 5 * round_n
    else:
        loot = 0
    return rounds, won, hero_health, loot


def buy(price, gold, quantity=1):
    """Покупает quantity штук товара ценой price за золото gold.
    quantity по умолчанию 1. Возвращает (gold_left, ok): остаток
    золота и признак успешной покупки. Ничего не печатает.
    """
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False


def print_leaderboard(log):
    """Печатает топ-3 раундов по урону героя и самый сильный удар врага.
    Возвращает None: задача функции - печать, а не данные.
    """
    if not log:
        print("Ты ещё ни с кем не сражался.")
        return
    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
    print(f"Таблица лидеров (урон героя, всего раундов: {len(log)}):")
    for i in range(len(top)):
        print(f"{i + 1}. Раунд {top[i][0]}: {top[i][1]:.1f}")
    # при равных ударах max вернёт первый из них, меня это устраивает
    worst = max(log, key=lambda r: r[2])
    print(f"Самый сильный удар врага: {worst[2]} (раунд {worst[0]}).")


def print_run_summary(log):
    """Печатает итог забега: общий и средний урон героя.
    Возвращает None. Работает и на пустом журнале.
    """
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Урон за забег: {total:.1f}, раундов: {rounds}, в среднем {total / rounds:.1f}.")
    else:
        print("В этом забеге боёв не было.")


running = True
menu_last = 9
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
        print("7 - спуститься глубже")
        print("8 - таблица лидеров")
        print("9 - лавка старого шахтёра")
        print("0 - подняться на поверхность")

        # --- Проверка пункта меню ---------------------
        while True:
            choice = input()
            try:
                menu_number = int(choice)
            except ValueError:
                print("Нет такого пункта. Введи номер из меню (0-9).")
                continue
            if 0 <= menu_number <= menu_last:
                choice = str(menu_number)
                break
            print("Нет такого пункта. Введи номер из меню (0-9).")

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
                    hit_damage, crit = hero_hit(i)
                    if crit:
                        crit_count += 1
                        print(f"Удар {i}: {hit_damage:.1f} - критический!")
                    else:
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

            case "7":
                if not enemies:
                    print("Ты спускаешься ниже, но шахта пуста: врагов больше нет.")
                else:
                    enemy = random.choice(enemies)
                    rounds, won, health, loot = fight(enemy, health, bonus=ability_bonus)
                    for r in rounds:
                        log.append(r)
                    if won:
                        gold_total += loot
                        enemies.remove(enemy)
                        print(f"Враг {enemy} побеждён! В шахте осталось врагов: {len(enemies)}. "
                              f"Добыча: {loot} золота.")
                    print(f"Бой длился раундов: {len(rounds)}.")
                    print(f"Последний раунд: урон героя {log[-1][1]:.1f}, урон врага {log[-1][2]}.")

            case "8":
                print_leaderboard(log)

            case "9":
                print("Лавка старого шахтёра:")
                print("(bandage - бинты +10 здоровья, lamp_oil - масло +5, pickaxe - кирка +2 к урону)")
                for name, price in prices.items():
                    print(f"{name}: {price} золота")
                print("Название товара (пустая строка - ничего не покупать):")
                name = input().strip()
                if name != "":
                    if name in prices:
                        price = prices[name]
                        print("Сколько штук (Enter - одна):")
                        while True:
                            qty_line = input()
                            if qty_line == "":
                                break
                            try:
                                if int(qty_line) > 0:
                                    break
                            except ValueError:
                                pass
                            print("Нужно целое число больше нуля или просто Enter:")
                        if qty_line == "":
                            qty = 1
                            gold_total, ok = buy(price, gold_total)
                        else:
                            qty = int(qty_line)
                            gold_total, ok = buy(price, gold_total, quantity=qty)
                        if ok:
                            if name == "lamp_oil":
                                # масло сразу заливаем в лампу
                                lamp_oil = min(lamp_oil + 5 * qty, max_oil)
                            else:
                                if name == "pickaxe":
                                    ability_bonus += 2 * qty
                                # BACKPACK
                            print(f"Куплено: {name} x{qty} за {price * qty} золота. Осталось золота: {gold_total}.")
                        else:
                            print(f"Не хватает золота: нужно {price * qty}, есть {gold_total}.")
                    else:
                        print("Такого товара в лавке нет.")

            case "0":
                print("Ты поднимаешься по лестнице к солнцу. Шахта остаётся внизу.")
                outcome = "выход"
                running = False

        if running:
            actions += 1

        # --- Состояние героя ---------------------------
        print()
        print(f"Здоровье: {health:4d}   Масло в лампе: {lamp_oil:3d}   Удача: {luck:3d}   Врагов: {len(enemies)}   Золото: {gold_total}")
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
    print_run_summary(log)
    print(frame)
