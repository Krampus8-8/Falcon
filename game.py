# ================================================
# ИГРА «ЗАБРОШЕННАЯ ШАХТА»
# Автор: Кашулинский Лев
# Дата: сентябрь 2026
#
# Пункт 4 - «постучать по стене» (knock): герой стучит
# по камню и по звуку ищет пустоты, за это растёт удача.
# Масло в лампе - это запас сил героя. Без света
# идти опасно: недостающее масло забирает здоровье.
# Новая кирка из лавки даёт +2 к урону за каждую купленную штуку,
# две кирки дают +4. Бинты и масло не поднимают выше стартового запаса.
# Команды можно вводить словами (go, buy bandage 2) или номерами.
# ================================================

import json
import os
import random

import dungeon

# цвет необязателен: без colorama игра работает обычным текстом
try:
    from colorama import Fore, Style, init
    init()
    COLOR = True
except ImportError:
    COLOR = False

# Lib5. Из документации colorama, не было на занятии:
# Fore.MAGENTA, Fore.CYAN, Fore.LIGHTYELLOW_EX - цвета текста;
# Style.BRIGHT (яркий текст) и Style.DIM (тусклый текст) - стили.
# Строка победы над врагом печатается Fore.LIGHTYELLOW_EX + Style.BRIGHT.

# --- Заголовок ------------------------------------
title = "ЗАБРОШЕННАЯ ШАХТА"
frame = "=" * 23
print(frame)
print("   " + title + "   ")
print(frame)
print()

# --- Сохранение: продолжить или начать заново -----
loaded = None
if os.path.exists("save.json"):
    print("Найдено сохранение. Продолжить забег? (да/нет)")
    answer = input().strip().lower()
    if answer in ("да", "yes"):
        try:
            with open("save.json", encoding="utf-8") as f:
                loaded = json.load(f)
        except json.JSONDecodeError:
            print("Файл сохранения испорчен, начинаем новый забег.")
            loaded = None

if loaded is None:
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

else:
    hero_name = loaded["hero"]
    health = loaded["health"]
    strength = loaded["strength"]
    agility = loaded["agility"]
    luck = loaded["luck"]

# --- Расчёт урона ----------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
# масло в лампе: сколько раз можно зажечь лампу.
# деление нацело, потому что половину раза зажечь нельзя
lamp_oil = (health + luck * 10) // 25
max_oil = lamp_oil
max_health = health

if loaded is None:
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

# --- Враги, журнал боя и рюкзак -------------------
# цены лавки и карточки врагов живут в dungeon.py
enemies = ["крыса-мутант", "шахтёр-призрак", "угольный голем", "летучая мышь"]
log = []
gold_total = 0
inventory = {}
ability_bonus = 0

# --- Карта шахты ----------------------------------
# "#" - стена, "." - штрек, "S" - клеть, в которой спустился герой.
# Рамка из стен обязательна: на неё опирается рекурсия scout,
# поэтому под клетью добавлен ещё один ряд стен.
MAP = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "#", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", "#", "S", ".", "#"],
    ["#", "#", "#", "#", "#"],
]
hero_r, hero_c = 4, 2
visited = {(4, 2)}
LOOT = {(1, 1): "старая каска", (2, 3): "кусок золотой руды", (3, 3): "фонарь бригадира"}
found_loot = set()
DIRECTIONS = {"north": (-1, 0), "south": (1, 0), "west": (0, -1), "east": (0, 1)}
DIR_NAMES = {"north": "север", "south": "юг", "west": "запад", "east": "восток"}

# --- Команды и меню -------------------------------
num_to_verb = {"1": "look", "2": "go", "3": "rest", "4": "knock",
               "5": "lamp", "6": "train", "7": "descend", "8": "leaders",
               "9": "shop", "10": "backpack", "11": "bandage", "12": "map",
               "13": "scout", "14": "newgame", "0": "exit"}
commands = ["look", "go", "go north/south/west/east", "rest", "knock", "lamp", "train", "descend",
            "leaders", "shop", "backpack", "bandage", "map", "scout", "newgame",
            "buy <товар> [количество]", "help", "exit"]
MENU = ["Что делаешь? (номер или команда, help - справка)",
        "1 - осмотреться (look)",
        "2 - идти вперёд (go)",
        "3 - отдохнуть (rest)",
        "4 - постучать по стене (knock)",
        "5 - зажечь шахтёрскую лампу (lamp)",
        "6 - тренировка (train)",
        "7 - спуститься глубже (descend)",
        "8 - таблица лидеров (leaders)",
        "9 - лавка старого шахтёра (shop)",
        "10 - рюкзак (backpack)",
        "11 - перевязать раны (bandage)",
        "12 - карта шахты (map)",
        "13 - разведать штреки (scout)",
        "14 - стереть сохранение (newgame)",
        "0 - подняться на поверхность (exit)"]


# --- Функции игры ---------------------------------
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


def write_save():
    """Собирает состояние забега и пишет его в save.json.
    Кортежи и множества превращает в списки: JSON их не знает.
    Читает глобальные переменные игры. Возвращает None.
    """
    save = {}
    save["hero"] = hero_name
    save["health"] = health
    save["strength"] = strength
    save["agility"] = agility
    save["luck"] = luck
    save["lamp_oil"] = lamp_oil
    save["max_oil"] = max_oil
    save["max_health"] = max_health
    save["gold"] = gold_total
    save["bonus"] = ability_bonus
    save["actions"] = actions
    save["enemies"] = enemies
    save["inventory"] = inventory
    save["log"] = log
    save["position"] = [hero_r, hero_c]
    save["visited"] = [list(p) for p in visited]
    save["loot"] = sorted(found_loot)
    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(save, f, ensure_ascii=False, indent=2)


def scout(r, c, seen):
    """Рекурсивно считает комнаты, достижимые из клетки (r, c).
    seen - множество уже посчитанных клеток, общее на весь обход.
    Возвращает число комнат. Ничего не печатает.
    """
    if (r, c) in seen or MAP[r][c] == "#":
        return 0
    seen.add((r, c))
    total = 1
    for dr, dc in DIRECTIONS.values():
        total += scout(r + dr, c + dc, seen)
    return total


# --- Главный цикл игры ----------------------------
running = True
outcome = "прерывание"
actions = 0

# --- Восстановление забега из сохранения ----------
if loaded is not None:
    lamp_oil = loaded["lamp_oil"]
    max_oil = loaded["max_oil"]
    max_health = loaded["max_health"]
    gold_total = loaded["gold"]
    ability_bonus = loaded["bonus"]
    actions = loaded["actions"]
    enemies = loaded["enemies"]
    inventory = loaded["inventory"]
    log = loaded["log"]
    hero_r, hero_c = loaded["position"]
    visited = {tuple(p) for p in loaded["visited"]}
    found_loot = set(loaded["loot"])
    print(f"Забег продолжен, {hero_name}: здоровье {health}, золото {gold_total}, врагов осталось {len(enemies)}.")
    print()

try:
    while running:
        print("\n".join(MENU))

        # --- Чтение и разбор команды -----------------
        line = input()
        cmd = line.strip().lower()
        while cmd == "":
            print("Пустая команда. Введи команду или номер пункта.")
            line = input()
            cmd = line.strip().lower()
        words = cmd.split()
        verb = words[0]
        if cmd in num_to_verb:
            verb = num_to_verb[cmd]

        # --- Выбор действия ----------------------------
        match verb:
            case "look":
                print("Ты осмотрелся. Ржавые рельсы уходят в темноту, рядом стоит перевёрнутая вагонетка.")

            case "go":
                if len(words) > 1 and words[1] in DIRECTIONS:
                    dr, dc = DIRECTIONS[words[1]]
                    nr, nc = hero_r + dr, hero_c + dc
                    if 0 <= nr < len(MAP) and 0 <= nc < len(MAP[nr]) and MAP[nr][nc] != "#":
                        hero_r, hero_c = nr, nc
                        visited.add((hero_r, hero_c))
                        print(f"Ты идёшь на {DIR_NAMES[words[1]]}. Штрек ({hero_r}, {hero_c}).")
                        if (hero_r, hero_c) in LOOT:
                            item = LOOT[(hero_r, hero_c)]
                            if item not in found_loot:
                                found_loot.add(item)
                                print(f"Ты нашёл: {item}! Уникальных находок: {len(found_loot)}.")
                    else:
                        print(f"Нельзя пройти на {DIR_NAMES[words[1]]}: там стена.")
                else:
                    cost = 2
                    if lamp_oil >= cost:
                        lamp_oil -= cost
                        print("Ты идёшь вперёд по рельсам. Под ногами хрустит уголь, лампа коптит.")
                    else:
                        health -= (cost - lamp_oil) * 10
                        lamp_oil = 0
                        print("Лампа погасла. Ты идёшь на ощупь и ударяешься о балки.")

            case "rest":
                # отдых даёт меньше, чем забирает дорога, и не больше полного запаса
                lamp_oil = min(lamp_oil + 1, max_oil)
                print("Ты присел на ящик из-под динамита и немного отдохнул.")

            case "knock":
                luck = luck + 1
                print("Ты стучишь по стене. В одном месте звук глухой: там пустота! Удача на твоей стороне.")

            case "lamp":
                if lamp_oil >= 1:
                    lamp_oil -= 1
                    health = health + 5
                    print("Ты зажёг лампу ярче. Стало светло и не так страшно, ты приободрился.")
                else:
                    print("Масла не осталось, лампа не зажигается.")

            case "train":
                strikes = 6
                total_damage = 0
                crit_count = 0
                print("В тупике висит старый мешок с углём.")
                print("Шахтёры били по нему кирками, когда спорили, кто сильнее.")
                print()
                print(f"Наносишь {strikes} ударов.")
                for i in range(1, strikes + 1):
                    hit_damage, crit = dungeon.hero_hit(i, damage, crit_damage)
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

            case "descend":
                if not enemies:
                    print("Ты спускаешься ниже, но шахта пуста: врагов больше нет.")
                else:
                    enemy = random.choice(enemies)
                    rounds, won, health, loot = dungeon.fight(enemy, health, ability_bonus, damage, crit_damage)
                    for r in rounds:
                        log.append(r)
                    if won:
                        gold_total += loot
                        enemies.remove(enemy)
                        victory = (f"Враг {enemy} побеждён! В шахте осталось врагов: {len(enemies)}. "
                                   f"Добыча: {loot} золота.")
                        if COLOR:
                            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + victory + Style.RESET_ALL)
                        else:
                            print(victory)
                    print(f"Бой длился раундов: {len(rounds)}.")
                    print(f"Последний раунд: урон героя {log[-1][1]:.1f}, урон врага {log[-1][2]}.")

            case "leaders":
                print_leaderboard(log)

            case "shop":
                print("Лавка старого шахтёра:")
                print("(bandage - бинты +10 здоровья, lamp_oil - масло +5, pickaxe - кирка +2 к урону)")
                for name, price in dungeon.prices.items():
                    print(f"{name}: {price} золота")
                print("Купить: buy <товар> [количество], например buy bandage 2")

            case "buy":
                if len(words) > 1 and words[-1].isdigit():
                    qty = int(words[-1])
                    item = " ".join(words[1:-1])
                else:
                    qty = 1
                    item = " ".join(words[1:])
                if item == "":
                    print("Что купить? Напиши: buy <товар>.")
                    continue
                if item not in dungeon.prices or qty < 1:
                    print("Такого товара в лавке нет.")
                    continue
                gold_total, ok = dungeon.buy(dungeon.prices[item], gold_total, quantity=qty)
                if ok:
                    if item == "lamp_oil":
                        # масло сразу заливаем в лампу
                        lamp_oil = min(lamp_oil + 5 * qty, max_oil)
                    else:
                        if item == "pickaxe":
                            ability_bonus += 2 * qty
                        inventory[item] = inventory.get(item, 0) + qty
                    print(f"Куплено: {item} x{qty} за {dungeon.prices[item] * qty} золота. Осталось золота: {gold_total}.")
                else:
                    print(f"Не хватает золота: нужно {dungeon.prices[item] * qty}, есть {gold_total}.")

            case "backpack":
                if not inventory:
                    print("Рюкзак пуст.")
                else:
                    print("В рюкзаке:")
                    for name, qty in inventory.items():
                        print(f"{name}: {qty} шт.")

            case "bandage":
                if inventory.get("bandage", 0) == 0:
                    print("В рюкзаке нет бинтов.")
                else:
                    health = min(health + 10, max_health)
                    inventory["bandage"] -= 1
                    if inventory["bandage"] == 0:
                        del inventory["bandage"]
                    print(f"Ты перевязал раны. Здоровье: {health}. Бинтов осталось: {inventory.get('bandage', 0)}.")

            case "map":
                print("Карта шахты (@ - ты):")
                for i in range(len(MAP)):
                    cells = []
                    for j in range(len(MAP[i])):
                        cell = "@" if (i, j) == (hero_r, hero_c) else MAP[i][j]
                        cells.append(cell)
                    print(" ".join(cells))
                print(f"Посещено штреков: {len(visited)}.")

            case "scout":
                seen = set()
                print(f"Разведка: можно дойти до {scout(hero_r, hero_c, seen)} штреков.")

            case "newgame":
                if os.path.exists("save.json"):
                    os.remove("save.json")
                    print("Сохранение стёрто. Следующий забег начнётся с чистого листа.")
                else:
                    print("Сохранения нет, стирать нечего.")
                continue

            case "help":
                print("Команды: " + ", ".join(commands) + ".")
                print("Номера 0-14 работают как раньше.")

            case "exit":
                print("Ты поднимаешься по лестнице к солнцу. Шахта остаётся внизу.")
                write_save()
                print("Прогресс сохранён.")
                outcome = "выход"
                running = False

            case _:
                print(f"Не понимаю команду: '{line.strip()}'. Напиши 'help'.")
                continue

        if running:
            actions += 1

        # --- Состояние героя ---------------------------
        print()
        state = (f"Здоровье: {health:4d}   Масло в лампе: {lamp_oil:3d}   Удача: {luck:3d}   "
                 f"Врагов: {len(enemies)}   Золото: {gold_total}")
        if COLOR:
            print(Fore.GREEN + state + Style.RESET_ALL)
        else:
            print(state)
        print()

        # --- Проверка гибели ---------------------------
        if health <= 0:
            print(f"{hero_name} падает в темноте. Шахта забирает ещё одного искателя.")
            if os.path.exists("save.json"):
                os.remove("save.json")
            outcome = "гибель"
            running = False
except KeyboardInterrupt:
    print()
    print("Игрок бросил кирку и убежал (Ctrl + C).")
    write_save()
    print("Прогресс сохранён.")
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
    if inventory:
        print("В рюкзаке осталось:")
        for name, qty in inventory.items():
            print(f"{name}: {qty} шт.")
    else:
        print("В рюкзаке осталось: ничего.")
    print(frame)
