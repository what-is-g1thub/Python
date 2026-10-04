rejected = 0
number = int(input(">> Введите целое число: "))

while number <= 0:
	rejected += 1
	number = int(input(">> Введите целое число: "))

print(f"Квадрат: {number ** 2}")
print(f"Отклонено: {rejected}")