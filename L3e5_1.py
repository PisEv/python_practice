# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
n = int(input("Введите размер массива членов Фибоначчи: "))

fib1 = 0
fib2 = 1
arr = [fib1, fib2]
res_arr = []

for i in range(n-1):
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    arr.append(fib_sum)

for j in range(len(arr)-1,0,-1):
    if j%2 == 0:
        res_arr.append(-arr[j])
    else:
        res_arr.append(arr[j])
res_arr += arr

print(res_arr)