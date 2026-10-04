n = int(input(">> Введите n >= 0: "))

count = 0
total = 0

for _ in range(n):
    number = int(input("Введите целое число: "))
    if abs(number) <= 3:
        count += 1
        total += number

print(f"Количество: {count}")
print(f"Сумма: {total}")
