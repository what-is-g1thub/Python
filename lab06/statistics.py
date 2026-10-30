numbers = [int(p) for p in input("Целые числа через пробел: ").split()]
if not numbers:
    print("Нет данных")
else:
    avg = sum(numbers) / len(numbers)
    print(f"Количество: {len(numbers)}")
    print(f"Сумма: {sum(numbers)}")
    print(f"Минимум: {min(numbers)}")
    print(f"Максимум: {max(numbers)}")
    print(f"Среднее: {avg:.2f}")