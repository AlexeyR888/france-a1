import random

while True:
    message = input("Введите сообщение: ")
    if "1" in message:
        colors = ["яблоко","банан","апельсин","персик","груша","виноград","клубника","вишня","ананас","малина",]
        random_color = random.choice(colors)
        print(random_color)
    else:
        print("Сообщение не содержит '1'.")
