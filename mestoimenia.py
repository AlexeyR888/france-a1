import random

while True:
    message = input("Введите сообщение: ")
    if "1" in message:
        colors = ["je", "tu", "il", "elle", "nous", "vous", "ils", "elles"]
        random_color = random.choice(colors)
        print(random_color)
    else:
        print("Сообщение не содержит '1'.")
