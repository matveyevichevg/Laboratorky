# функция проверки значения, принимает переменную неопределенного типа,
# возвращает True если это число и оно больше нуля, False во всех остальных случаях
def isPositiveNumber(num):
    try:
        if float(num):
            return True
        else:
            return False
    except ValueError:
        return False
while True:
    F = input('Введите градусы по фаренгейту: ')
    if isPositiveNumber(F):
        F=float(F)
        break
    else:
        print('Ошибка, ведите число')

C = float((5/9)*(int(F)-32))
print('По цельсию равно: {0:.1f} '.format(C))