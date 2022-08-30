# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def multiply():
    a = []
    count = 1
    x = int(input ('Введите число '))
    for i in range(1,x+1):
        count *= i
        a.append(count)
    print(a)


i = 0
while i < 9:
    multiply()
    i += 1
    print("осталось", 9-i, "попыток(ки)")