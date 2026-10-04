# Фрагмент А
# Ожидалось: 5 (сумма чисел). Ошибка: "2" + "3" даёт "23" (склейка строк).
first = "2"
second = "3"

first = int(first)
second = int(second)

print(first + second)

# Фрагмент Б
# Ожидалось: 18 при вводе 17. Ошибка: input() возвращает строку, "17" + 1 - питон кидает ошибку TypeError.
age = int(input("Возраст: "))
print(age + 1)

# Фрагмент В
# Ожидалось: 7.0. Ошибка: деление (third / 3) выполняется раньше сложения.
first = 4
second = 7
third = 10
average = (first + second + third) / 3
print(average)