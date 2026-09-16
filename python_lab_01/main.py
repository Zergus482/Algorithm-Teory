#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Импортируем модули-задания
import task_00_distance
import task_01_circle
import task_02_operations
import task_03_favorite_movies
import task_04_my_family
import task_05_zoo
import task_06_songs_list
import task_07_secret
import task_08_garden
import task_09_shopping
import task_10_store


def main():
    tasks = {
        '0': ('00_distance', task_00_distance.run),
        '1': ('01_circle', task_01_circle.run),
        '2': ('02_operations', task_02_operations.run),
        '3': ('03_favorite_movies', task_03_favorite_movies.run),
        '4': ('04_my_family', task_04_my_family.run),
        '5': ('05_zoo', task_05_zoo.run),
        '6': ('06_songs_list', task_06_songs_list.run),
        '7': ('07_secret', task_07_secret.run),
        '8': ('08_garden', task_08_garden.run),
        '9': ('09_shopping', task_09_shopping.run),
        '10': ('10_store', task_10_store.run),
    }

    while True:
        print("МЕНЮ")
        for key, (name, _) in tasks.items():
            print(f"[{key:>2}] {name}")
        print("[ q] Выход")
        print("-" * 40)

        choice = input("Выберите номер задания: ").strip().lower()

        if choice in ('q', 'exit'):
            print("Программа завершена.")
            break

        if choice in tasks:
            task_name, task_func = tasks[choice]
            print(f"\n--- Запуск: {task_name} ---")
            task_func()
            print("-" * 30)
        else:
            print("Неверный ввод, введите число от 0 до 10 или 'q'.")


if __name__ == '__main__':
    main()