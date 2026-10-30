numbers = [int(p) for p in input("Целые числа через пробел: ").split()]
selected = []
for n in numbers:
    if abs(n) <= 3:
        selected.append(n)
print(f"Выборка: {selected}")
print(f"Количество: {len(selected)}")
print(f"Сумма: {sum(selected)}")
print(f"Отсортировано: {sorted(selected)}")