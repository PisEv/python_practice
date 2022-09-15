# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

stroka = input().split()
for i in stroka:
    if i.find('абв') != -1:
        stroka.remove(i)
print(*stroka)