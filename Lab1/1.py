import math

def ex(f):
    try:
        if float(f) > 0:
            return True
        else:
            return False
    except ValueError:
        return False

while True:
    a = input('Веедите катет a: ' )
    if ex(a):
        a = float(a)
        break
    else:
        print('Ошибка, Введите положительное число')

while True:
    b = input('Веедите катет b: ' )
    if ex(b):
        b = float(b)
        break
    else:
        print('Ошибка, Введите положительное число')

gip = math.sqrt(a**2 + b**2)
print('Гипотенуза равна: {0:.1f} '.format(gip))


