"""Правила игры «Заброшенная шахта»: удар героя, бой, покупка, цены и карточки врагов.

Модуль не знает глобальных переменных game.py: урон героя и его здоровье
приходят параметрами. Случайный выбор врага (random.choice) остаётся
в game.py, потому что это часть сюжета, а не правило боя; здесь random
нужен только самотесту.
"""
import random

prices = {"bandage": 10, "lamp_oil": 15, "pickaxe": 40}

enemy_stats = {
    "крыса-мутант": {"hp": 30, "damage": 4, "loot": 15},
    "шахтёр-призрак": {"hp": 45, "damage": 6, "loot": 25},
    "угольный голем": {"hp": 60, "damage": 7, "loot": 35},
    "летучая мышь": {"hp": 15, "damage": 2, "loot": 5},
}


def hero_hit(strike_n, damage, crit_damage):
    """Урон героя в удар номер strike_n.
    Возвращает пару (hit, crit): урон и признак критического удара.
    Каждый третий удар критический.
    """
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False


def fight(enemy, hero_health, bonus, damage, crit_damage):
    """Бой с enemy до гибели одного из двоих.
    bonus - надбавка к урону героя, прибавляется после удвоения критом.
    damage и crit_damage - обычный и критический урон героя.
    Карточка врага берётся из enemy_stats по имени, в ней нужны ключи
    hp, damage и loot. Печатает строки раундов.
    Возвращает (rounds, won, hero_health, loot):
    таблицу раундов, признак победы, здоровье после боя и золото.
    """
    stats = enemy_stats[enemy]
    enemy_hp = float(stats["hp"])
    rounds = []
    round_n = 0
    print(f"Ты спускаешься по ржавой лестнице. Из темноты выходит {enemy}!")
    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n, damage, crit_damage)
        hit = hit + bonus
        enemy_hp -= hit
        line = f"Раунд {round_n}: ты наносишь {hit:.1f}"
        if crit:
            line += " - критический!"
        if enemy_hp <= 0:
            line += " Враг падает." if crit else ". Враг падает."
            rounds.append([round_n, hit, 0])
        else:
            enemy_hit = stats["damage"]
            hero_health -= enemy_hit
            line += f". У врага осталось {enemy_hp:.1f}. Ответный удар: {enemy_hit}."
            rounds.append([round_n, hit, enemy_hit])
        print(line)
    won = enemy_hp <= 0
    loot = stats["loot"] if won else 0
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

