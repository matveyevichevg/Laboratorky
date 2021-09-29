#Модуль для ввода и проверки введенного значения на положительное число


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
def getPositiveNumber(message):
    while True:
        n = input(message)
        if isPositiveNumber(n):
            n = float(n)
            return n
        else:
            print('Ошибка, Введитe положительное число')