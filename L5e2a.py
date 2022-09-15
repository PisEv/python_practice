# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?


import random

sweets = 100

corch = 1
chel = -1
print("Количество конфет ", sweets)

while sweets > 0:
    if corch == 1:
        chel = -1
        while chel > 28 or chel<0:
            chel = int(input("Введите от 1 до 28 "))
        sweets -= chel

        print("Количество конфет ", sweets)
        if sweets == 0:
            break
        corch = 0
    if corch == 0:
        if sweets <= 28:
            sweets = 0
        else:
            if sweets%29 == 0:
                comp = 28
            else:
                comp = sweets%29

            comp = random.randint(1,28)
            sweets -= comp
        corch = 1
        print("Бот забрал ", comp)
        print("Количество конфет ", sweets)
        if sweets == 0:
            break

if corch == 1:
    print("Вы победили")
else:
    print("Вы проиграли")


