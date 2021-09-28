import math

# функция проверки значения, принимает переменную неопределенного типа, возвращает True если это число и оно больше нуля, False во всех остальных случаях
def isPositiveNumber():
    try:
        if float(f) > 0:
            return True
        else:
            return False
    except ValueError:
        return False

# функция ввода значения катетов, принимает переменную а и b, возвращает их если они прошли проверку isPositiveNumber
def getPositiveNumber():
    while True:
        a = input('Веедите катет a: ' )
        if isPositiveNumber(a):
            a = float(a)
            return a
        else:
            print('Ошибка, Введите положительное число')
    while True:
        b = input('Веедите катет b: ' )
        if isPositiveNumber(b):
            b = float(b)
            return b
        else:
            print('Ошибка, Введите положительное число')

a=getPositiveNumber()
b=getPositiveNumber()

gip = math.sqrt(a**2 + b**2)
print('Гипотенуза равна: {0:.1f} '.format(gip))


