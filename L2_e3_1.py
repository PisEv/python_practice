# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму
n = int(input("Введите число "))
count = 0
mass = []
for i in range(1,n+1):
    ch = (1+1/i)**i
    mass.append(ch)
    count += ch
print(mass)
print(count)