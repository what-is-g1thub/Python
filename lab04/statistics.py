n = int(input(">> Введите n: "))

total = 0
positives = 0

first = int(input(">> Введите число: "))
total += first
if first > 0:
	positives += 1
maximum = first

for _ in range(n - 1):
	number = int(input(">> Введите число: "))
	total += number
	if number > 0:
		positives += 1
	if number > maximum:
		maximum = number

print(f"Сумма: {total}")
print(f"Положительных: {positives}")
print(f"Максимум: {maximum}")