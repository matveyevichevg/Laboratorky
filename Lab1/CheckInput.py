#Модуль для ввода и проверки введенного значения


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

# #Функция проверяет входное значение на число
# возвращает True если это число, False в случае если это строка
def isNumber(num):
    try:
        if float(num):
            return True
        else:
            return False
    except ValueError:
        return False

#Функция ввода значения и провекри его на число
#возвращает введенную переменную если она число
def getNumber(message):
    while True:
        n = input(message)
        if isNumber(n):
            n = float(n)
            return n
        else:
            print('Ошибка, Введитe число')

#Функция запрашивает ввод икс и игрек, проверяет их на то
# что введенное значение число, возвращает их в кортеж
def getCoordinate():
    x = getNumber('x = ')
    y = getNumber('y = ')
    return (x, y)

