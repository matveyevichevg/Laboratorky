import math

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

# функция ввода значения катетов, принимает переменную k ,
# возвращает ee если онa прошлa проверку isPositiveNumber
print('Введите зачения катетов')
def getPositiveNumber():
    while True:
        k = input('Катет равен: ' )
        if isPositiveNumber(k):
            k = float(k)
            return k
        else:
            print('Ошибка, Введите положительное число')

a=getPositiveNumber()
b=getPositiveNumber()

gip = math.sqrt(a**2 + b**2)
print('Гипотенуза равна: {0:.1f} '.format(gip))


