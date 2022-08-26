def check_quarter():
    Ax = int(input('Программа принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. Введите X координату точки A. Ax = '))
    Ay = int(input('Введите Y координату точки A. Ay = '))
    Bx = int(input('Введите X координату точки B. Bx = '))
    By = int(input('Введите Y координату точки B. By = '))

    RESULT = isqrt ((Bx-Ax)*(Bx-Ax)+(By-Ay)*(By-Ay))
    print(RESULT)

i = 0
while i < 9:
    check_quarter()
    i += 1
