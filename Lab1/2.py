import CheckInput

print('Программма определения свойства треугольника')

u1 = CheckInput.getPositiveNumber('Введите первый угол: ')
u2 = CheckInput.getPositiveNumber('Введите второй угол: ')

while float(u1) + float(u2) >= 180:
    print('Ошибка,введи значения углов заново')
    u1 = CheckInput.getPositiveNumber('Введите первый угол: ')
    u2 = CheckInput.getPositiveNumber('Введите второй угол: ')
else:
    if float(u1) == 90 or float(u2) == 90:
        print('Это прямоугольный треугольник')
    elif float(u1) > 90 or float(u2) > 90:
        print('Это тупоугольный треугольник')
    else:
        print('Это остроугольный треугольник')

