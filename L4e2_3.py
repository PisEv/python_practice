# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input())
stroka = ''

for i in range(k+1):
    if i == 0:
        stroka = stroka + str(random.randint(0,100)) + '*x^' + str(k-i)
    else:
        stroka = stroka + '+' + str(random.randint(0,100)) + '*x^' + str(k-i)

print(stroka)