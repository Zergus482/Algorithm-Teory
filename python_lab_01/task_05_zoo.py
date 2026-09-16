#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def run():
    # Есть список животных в зоопарке
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

    # Посадите медведя (bear) между львом и кенгуру
    # и выведите список на консоль
    zoo.insert(1, 'bear')
    print(zoo)


    # Добавьте птиц из списка birds в последние клетки зоопарка
    birds = ['rooster', 'ostrich', 'lark']
    # и выведите список на консоль
    zoo.extend(birds)
    print(zoo)

    # Уберите слона (elephant) из зоопарка
    # и выведите список на консоль
    zoo.remove('elephant')
    print(zoo)


    # Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
    # Номера при выводе должны быть 1-индексированными (первая клетка - номер 1).
    print(f"Лев сидит в клетке {zoo.index('lion') + 1}")
    print(f"Жаворонок сидит в клетке {zoo.index('lark') + 1}")


if __name__ == '__main__':
    run()