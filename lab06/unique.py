numbers = [int(p) for p in input("Целые числа через пробел: ").split()]
result = []
for n in numbers:
    if n not in result:
        result.append(n)
print(result)