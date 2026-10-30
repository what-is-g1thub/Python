# Лабораторная 7. Функции (вариант 11)

## Запуск
python main.py
python test_functions.py

## Описание
- sum_digits(number) — сумма цифр модуля числа.
- average(numbers) — среднее или None для пустого списка.
- normalize_text(text) — нижний регистр, один пробел между словами.
- select_numbers(numbers, threshold) — новый список n, где abs(n) == threshold (вариант 11).

## Проверки (test_functions.py)
- sum_digits(0)=0, sum_digits(507)=12, sum_digits(-507)=12
- average([]) is None, average([2,4,6])=4
- normalize_text("  ПРИВЕТ   Мир  ") == "привет мир", normalize_text("   ") == ""
- select_numbers([-5,0,2,5], 2) == [2]
- select_numbers([1,2,3,-2,-3], 2) == [2, -2]  (граница и рядом)
- select_numbers([2,2,5], 2) == [2, 2]          (повторы)
- исходный список сохраняется (сравнение с копией)
- пустой список → []

## Команда запуска тестов
python test_functions.py

## Демонстрация обнаружения ошибки
Если заменить в select_numbers условие `abs(n) == threshold` на `abs(n) > threshold`,
то assert select_numbers(control, 2) == [2] падает с AssertionError.
После возврата исправной версии проверки проходят.

## Ответы на вопросы защиты
- return возвращает значение в вызывающий код, print только выводит на экран.
- Параметр — имя в определении функции, локальная переменная — переменная внутри функции.
- Тест на границу (n = -2 при пороге 2) ловит ошибку со строгим неравенством.