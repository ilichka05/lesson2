2.1
password = input("Введите пароль: ")
povtor_password = input("Повторите пароль: ")
if password == povtor_password:
    print("Пароль принят")
else:
    print("Пароль не принят")
2.2
number = int(input("Введите номер места в плацкартном вагоне: "))
if number % 2 == 0:
    side = "верхнее" if number <= 36 else "нижнее"
    place_type = "боковое" if number % 4 == 0 or number % 4 == 1 else "купе"
else:
    side = "нижнее" if number <= 36 else "верхнее"
    place_type = "боковое" if number % 4 == 2 or number % 4 == 3 else "купе"
print(f"Место {number} - {place_type} место, {side}")
2.3
def years(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"Год {year} - високосный")
    else:
        print("Этот год не високосный")
year = int(input("Введите год для проверки: "))
years(year)
2.4
color1 = input("Введите первый основной цвет (красный, синий или желтый): ").lower()
color2 = input("Введите второй основной цвет (красный, синий или желтый): ").lower()
if color1 == "красный" and color2 == "синий" or color1 == "синий" and color2 == "красный":
    secondary_color = "фиолетовый"
elif color1 == "красный" and color2 == "желтый" or color1 == "желтый" and color2 == "красный":
    secondary_color = "оранжевый"
elif color1 == "синий" and color2 == "желтый" or color1 == "желтый" and color2 == "синий":
    secondary_color = "зеленый"
else:
    print("Ошибка! Введите правильные названия основных цветов: красный, синий, желтый.")
    exit()
print(f"При смешивании {color1} и {color2} получится {secondary_color}.")
