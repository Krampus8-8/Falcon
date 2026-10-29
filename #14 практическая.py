# 14 практическая. Модули и библиотеки. Задачи Lib1-Lib6
# Задачи этого занятия - шаги сборки проекта: dungeon.py, самотест,
# окружение .venv, colorama с откатом, цвета и docstring модуля.
# Это меню проверяет каждый шаг запуском.
import os
import subprocess
import sys

import dungeon

HERE = os.path.dirname(os.path.abspath(__file__))

try:
    from colorama import Fore, Style, init
    init()
    COLOR = True
except ImportError:
    COLOR = False


def paint(text, *codes):
    """Красит текст, если colorama есть; иначе возвращает текст как есть."""
    if not COLOR:
        return text
    return "".join(codes) + text + Style.RESET_ALL


while True:
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКАЯ 14. ВЫБЕРИТЕ НОМЕР ЗАДАЧИ")
    print("--- Разбираем вместе ---")
    print("1  - Lib1 (Правила перенесены в dungeon.py)")
    print("2  - Lib2 (Самотест модуля)")
    print("--- Делаем сами ---")
    print("3  - Lib3 (Окружение .venv и requirements.txt)")
    print("4  - Lib4 [СЛОЖНОЕ] (colorama с откатом)")
    print("5  - Lib5 (Цвета из документации)")
    print("6  - Lib6 (Docstring модуля и help)")
    print("0  - Выход")
    print("=" * 60)

    choice = input("Введите номер задачи: ").strip()

    if choice == "0":
        print("Программа завершена.")
        break

    elif choice == "1":
        # Lib1. В dungeon.py есть правила, а в game.py их больше нет.
        for name in ("fight", "buy", "prices", "enemy_stats"):
            print(f"dungeon.{name}:", "есть" if hasattr(dungeon, name) else "НЕТ")
        # с этапа 16 функция hero_hit стала методом strike класса Hero
        if hasattr(dungeon, "hero_hit"):
            print("dungeon.hero_hit: есть")
        else:
            print("dungeon.Hero.strike (бывшая hero_hit):", "есть" if hasattr(dungeon.Hero, "strike") else "НЕТ")
        game_code = open(os.path.join(HERE, "game.py"), encoding="utf-8").read()
        print("def fight в game.py:", "осталась" if "def fight" in game_code else "нет, перенесена")
        print("Вызов в game.py через модуль:", "dungeon.fight(" in game_code)

    elif choice == "2":
        # Lib2. python dungeon.py печатает самотест, а import - нет.
        # PYTHONIOENCODING нужен, чтобы русский текст дочерней программы
        # пришёл в UTF-8, а не в кодировке консоли Windows
        child_env = dict(os.environ, PYTHONIOENCODING="utf-8")
        result = subprocess.run([sys.executable, os.path.join(HERE, "dungeon.py")],
                                capture_output=True, text=True, encoding="utf-8", env=child_env)
        print("Запуск python dungeon.py:")
        print(result.stdout.strip())
        print("При import dungeon имя модуля:", dungeon.__name__, "- самотест не запускался")

    elif choice == "3":
        # Lib3. Окружение проекта и файл зависимостей.
        venv = os.path.join(HERE, ".venv")
        print("Папка .venv:", "есть" if os.path.isdir(venv) else "нет (создай: python -m venv .venv)")
        req = os.path.join(HERE, "requirements.txt")
        if os.path.exists(req):
            print("requirements.txt:", open(req, encoding="utf-8").read().strip())
        print("Сейчас работает интерпретатор:", sys.executable)
        print("colorama доступна:", COLOR)
        print("Проверка изоляции: pip show colorama внутри .venv отвечает, а вне его - нет.")

    elif choice == "4":
        # Lib4. Импорт в try, флаг COLOR проверяется при печати.
        state = "Здоровье: 100   Масло в лампе: 5"
        if COLOR:
            print(Fore.GREEN + state + Style.RESET_ALL)
            print("(colorama найдена, строка зелёная)")
        else:
            print(state)
            print("(colorama не найдена, игра печатает обычный текст и не падает)")

    elif choice == "5":
        # Lib5. Три цвета Fore и две константы Style, которых не было на занятии.
        print(paint("Fore.MAGENTA - пурпурный", Fore.MAGENTA if COLOR else ""))
        print(paint("Fore.CYAN - голубой", Fore.CYAN if COLOR else ""))
        print(paint("Fore.LIGHTYELLOW_EX - светло-жёлтый", Fore.LIGHTYELLOW_EX if COLOR else ""))
        print(paint("Style.BRIGHT - яркий текст", Style.BRIGHT if COLOR else ""))
        print(paint("Style.DIM - тусклый текст", Style.DIM if COLOR else ""))
        print(paint("Враг побеждён!", *(Fore.LIGHTYELLOW_EX, Style.BRIGHT) if COLOR else ""))
        print("После каждой строки стоит Style.RESET_ALL, поэтому цвет дальше не тянется.")

    elif choice == "6":
        # Lib6. Docstring модуля - первая строка help(dungeon).
        print("dungeon.__doc__, первая строка:")
        print(dungeon.__doc__.splitlines()[0])

    else:
        print("Неверный ввод! Выберите номер из списка.")

    input("\nНажмите Enter для возврата в меню...")
