# функция проверки значения, принимает переменную неопределенного типа,
# возвращает True если это число и оно больше нуля, False во всех остальных случаях
def isPositiveNumber(num):
    try:
        if float(num) > 0:
            return True
        else:
            return False
    except ValueError:
        return False
# функция ввода значения угла, принимает переменную Angle ,
# возвращает ee если онa прошлa проверку isPositiveNumber
def getAngle():
    while True:
        Angle = input('Введи угол: ' )
        if isPositiveNumber(Angle):
            Angle=float(Angle)
            return (Angle)
        else:
            print('Ошибка, введите положительное число')

u1 = getAngle()
u2 = getAngle()

while float(u1) + float(u2) >= 180:
    print('Ошибка,введи значения углов заново')
    u1 = getAngle()
    u2 = getAngle()
else:
    if float(u1) == 90 or float(u2) == 90:
        print('Это прямоугольный треугольник')
    elif float(u1) > 90 or float(u2) > 90:
        print('Это тупоугольный треугольник')
    else:
        print('Это остроугольный треугольник')

