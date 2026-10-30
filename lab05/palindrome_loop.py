text = input("Введите текст: ")
cleaned = text.replace(" ", "").lower()
if not cleaned:
    print("Нет текста")
else:
    is_pal = True
    half = len(cleaned) // 2
    for i in range(half):
        if cleaned[i] != cleaned[-1 - i]:
            is_pal = False
            break
    print("Палиндром" if is_pal else "Не палиндром")