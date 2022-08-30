def check_day_of_week():
    a = int(input('Введите число для недели '))
    if a == 1 or a == 2 or a == 3 or a == 4 or a == 5:
        print('не выходной')
    elif a == 6 or a == 7:
        print('выходный')
    else:
        print('введите число от 1 до 7')


i = 0
while i < 9:
    check_day_of_week()
    i += 1


x = 3
while x > 0 and x < 8:
    x = int(input())
    if x > 5 and x < 8:
        print("Выходной")
    elif x <= 5 and x > 0:
        print("Не выходной")
    else:
        print("Некорректный ввод")