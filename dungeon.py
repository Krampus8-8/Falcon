"""Правила игры «Заброшенная шахта»: герой, враги, бой, покупка, цены и карточки врагов.

Модуль не знает глобальных переменных game.py: всё нужное приходит
параметрами или живёт в объектах Hero и Enemy. Случайный выбор врага
(random.choice) остаётся в game.py, потому что это часть сюжета, а не
правило боя; здесь random нужен только самотесту.
"""
import random

prices = {"bandage": 10, "lamp_oil": 15, "pickaxe": 40}

enemy_stats = {
    "крыса-мутант": {"hp": 30, "damage": 4, "loot": 15},
    "шахтёр-призрак": {"hp": 45, "damage": 6, "loot": 25},
    "угольный голем": {"hp": 60, "damage": 7, "loot": 35},
    "летучая мышь": {"hp": 15, "damage": 2, "loot": 5},
}


class Hero:
    """Герой забега: характеристики, урон и запас масла в лампе."""

    def __init__(self, name, health, strength, agility, luck):
        """Раскладывает характеристики по атрибутам и считает урон и масло."""
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.luck = luck
        self.damage = 10 + strength * 1.5
        self.crit_damage = self.damage * 2
        # деление нацело, потому что половину раза лампу не зажечь
        self.lamp_oil = (health + luck * 10) // 25

    def __str__(self):
        """Короткий формуляр героя одной строкой."""
        return (f"{self.name}: здоровье {self.health}, урон {self.damage:.1f}, "
                f"масло {self.lamp_oil}, удача {self.luck}")

    def strike(self, n):
        """Урон в удар номер n. Возвращает пару (урон, крит): каждый третий удар критический."""
        if n % 3 == 0:
            return self.crit_damage, True
        return self.damage, False

    def spend_oil(self, cost):
        """Тратит cost масла. Если масла не хватает, недостающее берётся
        из здоровья (по 10 за единицу), масло обнуляется.
        Возвращает True, если пришлось идти в темноте, иначе False.
        """
        if self.lamp_oil >= cost:
            self.lamp_oil -= cost
            return False
        self.health -= (cost - self.lamp_oil) * 10
        self.lamp_oil = 0
        return True

    def heal(self, amount, cap):
        """Лечит на amount, но не выше потолка cap. Возвращает None."""
        self.health = min(self.health + amount, cap)

    def to_dict(self):
        """Словарь для сохранения: текущее состояние и характеристики настройки."""
        return {"name": self.name, "health": self.health, "lamp_oil": self.lamp_oil,
                "strength": self.strength, "agility": self.agility, "luck": self.luck}

    @staticmethod
    def from_dict(data):
        """Создаёт героя из словаря сохранения и возвращает текущее масло."""
        hero = Hero(data["name"], data["health"], data["strength"],
                    data["agility"], data["luck"])
        hero.lamp_oil = data["lamp_oil"]
        return hero


class Enemy:
    """Враг на один бой: рабочая копия карточки из enemy_stats."""

    def __init__(self, name, stats):
        """name - имя врага, stats - карточка с ключами hp, damage и loot."""
        self.name = name
        self.hp = stats["hp"]
        self.damage = stats["damage"]
        self.loot = stats["loot"]


def fight(enemy, hero, bonus=0):
    """Бой врага enemy (объект Enemy) с героем hero (объект Hero).
    bonus - надбавка к урону героя, прибавляется после удвоения критом.
    Здоровье героя и врага меняется прямо в объектах. Печатает раунды.
    Возвращает (rounds, won, loot): таблицу раундов, признак победы и золото.
    """
    rounds = []
    round_n = 0
    print(f"Ты спускаешься по ржавой лестнице. Из темноты выходит {enemy.name}!")
    while enemy.hp > 0 and hero.health > 0:
        round_n += 1
        hit, crit = hero.strike(round_n)
        hit = hit + bonus
        enemy.hp -= hit
        line = f"Раунд {round_n}: ты наносишь {hit:.1f}"
        if crit:
            line += " - критический!"
        if enemy.hp <= 0:
            line += " Враг падает." if crit else ". Враг падает."
            rounds.append([round_n, hit, 0])
        else:
            hero.health -= enemy.damage
            line += f". У врага осталось {enemy.hp:.1f}. Ответный удар: {enemy.damage}."
            rounds.append([round_n, hit, enemy.damage])
        print(line)
    won = enemy.hp <= 0
    loot = enemy.loot if won else 0
    return rounds, won, loot


def buy(price, gold, quantity=1):
    """Покупает quantity штук товара ценой price за золото gold.
    quantity по умолчанию 1. Возвращает (gold_left, ok): остаток
    золота и признак успешной покупки. Ничего не печатает.
    """
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False


if __name__ == "__main__":
    test_hero = Hero("Тест", 100, 7, 5, 4)
    test_name = random.choice(list(enemy_stats))
    rounds, won, loot = fight(Enemy(test_name, enemy_stats[test_name]), test_hero)
    print(f"самотест: раундов {len(rounds)}, победа={won}, добыча={loot}, здоровье героя {test_hero.health}")
