order_name = input(">> Название заказа: ")
customer_name = input(">> Имя заказчика: ")

item1_name = input(">> Название первой позиции: ")
item1_quantity = int(input(">> Количество первой позиции: "))
item1_price = float(input(">> Цена единицы первой позиции (руб.): "))

item2_name = input(">> Название второй позиции: ")
item2_quantity = int(input(">> Количество второй позиции: "))
item2_price = float(input(">> Цена единицы второй позиции (руб.): "))

delivery_cost = float(input(">> Стоимость доставки (руб.): "))
discount_percent = float(input(">> Скидка в процентах (0-100): "))

item1_cost = item1_quantity * item1_price
item2_cost = item2_quantity * item2_price
goods_cost = item1_cost + item2_cost

discount_amount = goods_cost * discount_percent / 100
total_cost = goods_cost - discount_amount + delivery_cost

paid_amount = float(input(f">> Внесённая сумма (руб.) не меньше {total_cost:.2f}: "))

total_quantity = item1_quantity + item2_quantity
change = paid_amount - total_cost

print(f"====== Заказ: {order_name} ======")
print(f"Заказчик: {customer_name}")
print("Название | Количество | Цена | Стоимость")
print(f"{item1_name} | {item1_quantity} | {item1_price:.2f} | {item1_cost:.2f}")
print(f"{item2_name} | {item2_quantity} | {item2_price:.2f} | {item2_cost:.2f}")
print(f"Стоимость товаров без доставки: {goods_cost:.2f} руб.")
print(f"Скидка ({discount_percent:.2f}%): {discount_amount:.2f} руб.")
print(f"Стоимость доставки: {delivery_cost:.2f} руб.")
print(f"Итоговая сумма со скидкой и доставкой: {total_cost:.2f} руб.")
print(f"Общее количество единиц: {total_quantity}")
print(f"Сдача: {change:.2f} руб.")
