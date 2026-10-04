value = int(input(">> Введите заполненность парковки от 0 до 100: "))

if value < 0 or value > 100:
    print("Ошибка диапазона")
elif value <= 59:
    print("Много мест")
elif value <= 89:
    print("Мало мест")
else:
    print("Почти занята")
