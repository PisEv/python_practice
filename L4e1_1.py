# Вычислить число c заданной точностью d

def f_round():
    import math
    d = input("Введите точность вывода числа Пи в формате 0.0001: ")
    print(round(math.pi, len(d)-2))

i = 0
while i < 9:
    f_round()
    i += 1