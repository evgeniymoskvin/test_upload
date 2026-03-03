import os

a = input('Введите число')
try:
    a = int(a)
    for i in range(a):
        print(i)
except Exception as e:
    print(e)

