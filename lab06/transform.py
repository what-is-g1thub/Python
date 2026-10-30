numbers = [int(p) for p in input("Целые числа через пробел: ").split()]
result = []
for n in numbers:
    result.append(-n if n < 0 else n)
print(f"Исходный: {numbers}")
print(f"Новый: {result}")