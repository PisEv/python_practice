# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
def summary():
    x = input ('Введите число ')
    count = 0
    for i in range (len(x)):
        count += int(x[i])
    print(count)


i = 0
while i < 9:
    summary()
    i += 1
    print("осталось", 9-i, "попыток(ки)")