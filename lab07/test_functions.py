from functions import average, normalize_text, sum_digits, select_numbers

# --- базовые ---
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

# --- вариант 11: |n| == threshold ---
control = [-5, 0, 2, 5]
assert select_numbers(control, 2) == [2]
assert select_numbers([], 2) == []
# граница и рядом: |n| == 2
assert select_numbers([1, 2, 3, -2, -3], 2) == [2, -2]
# повторы сохраняются
assert select_numbers([2, 2, 5], 2) == [2, 2]
# исходный список не изменяется
control_copy = control.copy()
select_numbers(control, 2)
assert control == control_copy
# порог 0: подходит только 0
assert select_numbers([0, 1, -1, 5], 0) == [0]

# дробное среднее
actual = average([1, 2])
assert abs(actual - 1.5) < 1e-9

print("Базовые проверки пройдены")