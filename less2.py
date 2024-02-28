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
