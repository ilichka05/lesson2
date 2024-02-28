number = int(input("Введите номер места в плацкартном вагоне: "))
if number % 2 == 0:
    side = "верхнее" if number <= 36 else "нижнее"
    place_type = "боковое" if number % 4 == 0 or number % 4 == 1 else "купе"
else:
    side = "нижнее" if number <= 36 else "верхнее"
    place_type = "боковое" if number % 4 == 2 or number % 4 == 3 else "купе"
print(f"Место {number} - {place_type} место, {side}")
