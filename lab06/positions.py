numbers = [int(p) for p in input("Целые числа через пробел: ").split()]
if not numbers:
    print("Нет данных")
else:
    maximum = max(numbers)
    positions = []
    for i, value in enumerate(numbers):
        if value == maximum:
            positions.append(i)
    print(positions)