def check_quarter():
    quarter = int(input('Введите номер четверти = '))

    if quarter == 1:
        print('X>0; Y>0')
    elif quarter == 2:
        print('X<0; Y>0')
    elif quarter == 3:
        print('X<0; Y<0')
    elif quarter == 4:
        print('X>0; Y<0')
    else:
        print('Номер четверти должен быть в диапазоне от 1 до 4')

i = 0
while i < 9:
    check_quarter()
    i += 1
