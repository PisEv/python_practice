def check_XYZ():
    X = int(input('Введите X = '))
    Y = int(input('Введите Y = '))
    if X < 0 and Y < 0:
        print('3')
    elif X < 0 and Y > 0:
        print('2')
    elif X > 0 and Y < 0:
        print('4')
    elif X > 0 and Y > 0:
        print('1')
    else:
        print('X и Y должны быть > 0')

i = 0
while i < 9:
    check_XYZ()
    i += 1
