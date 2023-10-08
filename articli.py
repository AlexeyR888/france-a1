import random

while True:
    message = input("Введите сообщение: ")
    if "1" in message:
        colors = ["opr mug", "opr jen", "opr mng", "neo mug", "neo jen", "neo mng", "cst mug", "cst jen"]
        random_color = random.choice(colors)
        print(random_color)
    else:
        print("Сообщение не содержит '1'.")
