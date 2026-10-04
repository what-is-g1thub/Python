first_room = "А-101"
second_room = "Б-202"

print("До обмена:")
print("first_room:", first_room)
print("second_room:", second_room)

temp = second_room
second_room = first_room
first_room = temp

print("\nПосле обмена:")
print("first_room:", first_room)
print("second_room:", second_room)
