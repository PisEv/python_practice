# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите число для которых будут найдены простые множители: "))
arr = []
i = 2
while n != 1 :
    if n % i == 0:
        arr.append(i)
        n = n//i
    else:
        i += 1


print(arr)