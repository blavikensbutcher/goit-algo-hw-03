import argparse
import shutil
from pathlib import Path


def copy_and_sort_files(source_dir: Path, dist: Path):
    try:
        for item in source_dir.iterdir():
            if item.is_dir():
                copy_and_sort_files(item, dist)
            elif item.is_file():
                ext = item.suffix[1:] if item.suffix else "no_extension"
                target_subdir = dist / ext
                target_subdir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, target_subdir / item.name)
    except Exception as e:
        print(f"Помилка {source_dir}: {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=str)
    parser.add_argument("destination", nargs="?", default="dist")
    args = parser.parse_args()

    source_path = Path(args.source).resolve()
    destination_path = Path(args.destination).resolve()

    if not source_path.exists() or not source_path.is_dir():
        print(f"{source_path} не існує або не є папкою")
        return

    destination_path.mkdir(parents=True, exist_ok=True)

    copy_and_sort_files(source_path, destination_path)
    print(f"Копіювання завершено. Результат у: {destination_path}")


if __name__ == "__main__":
    main()

# Завдання 1
# Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії та сортує в піддиректорії, назви яких базуються на розширенні файлів.
#
# Також візьміть до уваги наступні умови:
#
# 1. Парсинг аргументів. Скрипт має приймати два аргументи командного рядка: шлях до вихідної директорії та шлях до директорії призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).
#
# 2. Рекурсивне читання директорій:
# Має бути написана функція, яка приймає шлях до директорії як аргумент.
# Функція має перебирати всі елементи у директорії.
# Якщо елемент є директорією, функція повинна викликати саму себе рекурсивно для цієї директорії.
# Якщо елемент є файлом, він має бути доступним для копіювання.
#
# 3. Копіювання файлів:
# Для кожного типу файлів має бути створений новий шлях у вихідній директорії, використовуючи розширення файлу для назви піддиректорії.
# Файл з відповідним типом має бути скопійований у відповідну піддиректорію.
#
# 4. Обробка винятків. Код має правильно обробляти винятки, наприклад, помилки доступу до файлів або директорій.
