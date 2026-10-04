subject1 = input(">> Название первого предмета: ")
subject2 = input(">> Название второго предмета: ")

count1 = int(input(f">> Количество занятий по предмету '{subject1}' за неделю: "))
count2 = int(input(f">> Количество занятий по предмету '{subject2}' за неделю: "))

duration1 = int(input(f">> Продолжительность одного занятия по предмету '{subject1}' (мин): "))
duration2 = int(input(f">> Продолжительность одного занятия по предмету '{subject2}' (мин): "))

time1 = count1 * duration1
time2 = count2 * duration2

total_minutes = time1 + time2
total_hours = total_minutes / 60

available_hours = float(input(f">> Доступное время на неделю (в часах, не меньше {total_hours:.2f} ч): "))
free_hours = available_hours - total_hours

four_weeks_minutes = total_minutes * 4
four_weeks_hours = four_weeks_minutes / 60

print(f"\n{subject1}: {time1} мин")
print(f"{subject2}: {time2} мин")
print(f"Общая нагрузка: {total_minutes} мин = {total_hours:.2f} ч")
print(f"Остаток свободного времени: {free_hours:.2f} ч")
print(f"Нагрузка за 4 недели: {four_weeks_minutes} мин = {four_weeks_hours:.2f} ч")
