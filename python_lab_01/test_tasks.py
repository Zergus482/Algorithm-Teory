import pytest
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


def test_distance(capsys):
    """Тест расчета расстояний между городами."""
    task_00_distance.run()
    captured = capsys.readouterr().out
    assert "'Moscow': {'London': 145.6, 'Paris': 130.38}" in captured
    assert "'London': {'Moscow': 145.6, 'Paris': 42.43}" in captured


def test_circle(capsys):
    """Тест площади круга и попадания точек."""
    task_01_circle.run()
    output_lines = [line.strip() for line in capsys.readouterr().out.strip().split('\n')]
    
    # Площадь: 3.1415926 * 42^2 = 5541.7693
    assert output_lines[0] == '5541.7693'
    # Точка 1: sqrt(23^2 + 34^2) ≈ 41.04 <= 42 -> True
    assert output_lines[1] == 'True'
    # Точка 2: sqrt(30^2 + 30^2) ≈ 42.42 <= 42 -> False
    assert output_lines[2] == 'False'


def test_operations(capsys):
    """Тест арифметического выражения (должно быть 25)."""
    task_02_operations.run()
    output_lines = [line.strip() for line in capsys.readouterr().out.strip().split('\n')]
    assert output_lines[0] == '9'
    assert output_lines[1] == '25'


def test_favorite_movies(capsys):
    """Тест срезов названий фильмов."""
    task_03_favorite_movies.run()
    output_lines = [line.strip() for line in capsys.readouterr().out.strip().split('\n')]
    assert output_lines[0] == 'Терминатор'
    assert output_lines[1] == 'Назад в будущее'
    assert output_lines[2] == 'Пятый элемент'
    assert output_lines[3] == 'Чужие'


def test_my_family(capsys):
    """Тест расчета роста отца и общего роста семьи."""
    task_04_my_family.run()
    captured = capsys.readouterr().out
    assert 'Рост отца - 182 см' in captured
    # 182 + 168 + 187 + 154 = 691
    assert 'Общий рост моей семьи - 691 см' in captured


def test_zoo(capsys):
    """Тест операций над списком животных зоопарка."""
    task_05_zoo.run()
    captured = capsys.readouterr().out
    assert "Лев сидит в клетке 1" in captured
    assert "Жаворонок сидит в клетке 7" in captured


def test_songs_list(capsys):
    """Тест суммирования времени песен."""
    task_06_songs_list.run()
    captured = capsys.readouterr().out
    # 'Halo' (4.9) + 'Enjoy the Silence' (4.2) + 'Clean' (5.83) = 14.93
    assert 'Три песни звучат 14.93 минут' in captured
    # 'Sweetest Perfection' (4.43) + 'Policy of Truth' (4.88) + 'Blue Dress' (4.18) = 13.49
    assert 'А другие три песни звучат 13.49 минут' in captured


def test_secret_message(capsys):
    """Тест расшифровки секретного сообщения."""
    task_07_secret.run()
    captured = capsys.readouterr().out.strip()
    assert captured == 'в бане веник дороже денег'


def test_garden(capsys):
    """Тест операций с множествами цветов."""
    task_08_garden.run()
    output_lines = [line.strip() for line in capsys.readouterr().out.strip().split('\n')]
    
    # Преобразуем строковые представления множеств обратно в set для устойчивости к порядку элементов
    all_flowers = eval(output_lines[0])
    both = eval(output_lines[1])
    only_garden = eval(output_lines[2])
    only_meadow = eval(output_lines[3])

    assert both == {'ромашка', 'одуванчик'}
    assert only_garden == {'роза', 'гладиолус', 'подсолнух'}
    assert only_meadow == {'клевер', 'мак'}
    assert all_flowers == {'ромашка', 'роза', 'одуванчик', 'гладиолус', 'подсолнух', 'клевер', 'мак'}


def test_shopping(capsys):
    """Тест словаря цен с двумя минимальными магазинами."""
    task_09_shopping.run()
    captured = capsys.readouterr().out
    sweets_dict = eval(captured.strip())
    
    assert 'печенье' in sweets_dict
    assert sweets_dict['конфеты'][0]['shop'] == 'магнит'
    assert sweets_dict['конфеты'][0]['price'] == 30.99


def test_store(capsys):
    """Тест расчета остатков товаров на складе."""
    task_10_store.run()
    captured = capsys.readouterr().out
    # Лампа: 27 шт * 42 = 1134 руб
    assert 'Лампа - 27 шт, стоимость 1134 руб' in captured
    # Стол: (22 * 510) + (32 * 520) = 11220 + 16640 = 27860 руб
    assert 'Стол - 54 шт, стоимость 27860 руб' in captured