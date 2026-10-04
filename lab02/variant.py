total = int(input(">> Общий объём: "))
capacity = int(input(">> Вместимость одной единицы: "))

full = total // capacity
remainder = total % capacity
min_units = (total + capacity - 1) // capacity

print(f"Полных единиц: {full}")
print(f"Остаток: {remainder}")
print(f"Минимальное число единиц: {min_units}")