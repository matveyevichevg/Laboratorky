def ex(f):
    try:
        if float(f) > 0:
            return True
        else:
            return False
    except ValueError:
        return False
while True:
    u1 = input('Введи первый угол: ' )
    if ex(u1):
        a=float(u1)
        break
    else:
        print('Ошибка, Введите положительное число')
while True:
    u2 = input('Введи второй угол: ' )
    if ex(u2):
        a=float(u2)
        break
    else:
        print('Ошибка, Введите положительное число')
if int(u1) + int(u2) == 180:
    print('Ошибка')
elif int(u1) == 90 or int(u2) == 90:
    print('Это прямоугольный треугольник')
elif int(u1) > 90 or int(u2) > 90:
    print('Это тупоугольный треугольник')
else:
    print('Это остроугольный треугольник')

