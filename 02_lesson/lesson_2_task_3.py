import math


def square(a):
    return math.ceil(a*a)


b = float(input('Введите сторону квадрата: '))
print(f'Округленная в большую сторону сумма - {square(b)}')
