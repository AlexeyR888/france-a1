import random

while True:
    message = input("Введите сообщение: ")
    if "1" in message:
        colors = ["слева", "справа", "спереди", "сзади", "снизу", "в", "рядом", "напротив", "над", "между", "среди", "под", "сверху"]
        random_color = random.choice(colors)
        print(random_color)
    else:
        print("Сообщение не содержит '1'.")
