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
        if int(num) == 0:
            return num
        elif float(num):
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


# функция проверки значения, принимает переменную неопределенного типа,
# возвращает True если это число и оно больше нуля, False во всех остальных случаях
def isPositiveNumber_int(num):
    try:
        if int(num) >= 0:
            return True
        else:
            return False
    except ValueError:
        return False


# функция ввода значения, принимает переменную n ,
# возвращает ee если онa прошлa проверку isPositiveNumber
def getPositiveNumber_int(message):
    while True:
        n = input(message)
        if isPositiveNumber_int(n):
            n = int(n)
            return n
        else:
            print('Ошибка, Введитe целое положительное число')
# #Функция проверяет входное значение на чцелочисленное значение
# возвращает True если это целочисленное значение, False в случае если это строка
def isNumber_int(num):
    try:
        if int(num) == 0:
            return num
        elif int(num):
            return True
        else:
            return False
    except ValueError:
        return False

#Функция ввода значения и провекри его на целочисленное значение
#возвращает введенную переменную если она целое число
def getNumber_int(message):
    while True:
        n = input(message)
        if isNumber_int(n):
            n = int(n)
            return n
        else:
            print('Ошибка, Введитe целочисленное значение')

#Функция ввода размера целочисленного массива и его значений, возвращает массив
def arrayInput_int():

    data_array = []
    n = getPositiveNumber_int('Введите размер массива ')

    while n == 0:
        print('Введите положительное значение')
        n = getPositiveNumber_int('Введите размер массива ')
    for i in range(int(n)):
        data_array.append(getNumber_int('Введите '+ str(i) +' элемент массива '))
    return data_array

#Функция ввода размера массива и его значений, возвращает массив
def arrayInput():

    data_array = []
    n = getPositiveNumber('Введите размер массива ')

    while n == 0:
        print('Введите положительное значение')
        n = getPositiveNumber_int('Введите размер массива ')
    for i in range(int(n)):
        data_array.append(getNumber('Введите '+ str(i) +' элемент массива '))
    return data_array



#Функция ввода пункта меню
def menu():
    userchoise = getNumber_int('Введите пункт меню цифрой:\n\n1. Ввод элементов массива\n2. Обработка массива\n3. Вывод массива на экран\n4. Выход\n')
    while userchoise < 1 or userchoise > 4:
        print('Ошибка, укажите существующий пункт меню')
        userchoise = getNumber_int('Введите пункт меню цифрой:\n1. Ввод элементов массива\n2. Обработка массива\n3. Вывод массива на экран\n4. Выход\n')
    return userchoise

