# Вариант 1
# В одномерном массиве целых чисел заменить минимальное значение средним арифметическим его элементов, находящихся на четных позициях.
import CheckInput
import numpy as np

#Ввод элементов массива
def vvod():
    array = CheckInput.arrayInput()
    return array

#Заменяет минимальное значение, средним арифмитическим его элементов, находящихся на четных позициях
def obrabortka(array):
    #Вычисление ср. арифметического
    average = np.average(array[::2])
    #Поиск индекса минимального значения в массиве
    minArgument = np.argmin(array)
    #Замена минимального значения средним арифмитическим его элементов, находящихся на четных позициях
    array[minArgument] = (average)

#Вывод значений массива на экран
def vyvod(array):
    print(array)

#Функция ввода пункта меню
def menu():
    userchoise = CheckInput.getNumber_int('Введите пункт меню цифрой:\n\n1. Ввод элементов массива\n2. Обработка массива\n3. Вывод массива на экран\n4. Выход\n')
    while userchoise < 1 or userchoise > 4:
        print('Ошибка, укажите существующий пункт меню')
        userchoise = CheckInput.getNumber_int('Введите пункт меню цифрой:\n1. Ввод элементов массива\n2. Обработка массива\n3. Вывод массива на экран\n4. Выход\n')
    return userchoise


choise = menu()

#Ограничение на ввод пункта меню, вначале всегда может быть только 1 или 4.
while choise  >= 2 and choise < 4:
    print('Ошибка, сначала надо ввести массив, выберите пункт 1')
    print()
    choise = menu()

#Реализация
while choise == 1:
    a = vvod()
    print()
    choise = menu()
    while choise == 2:
        obrabortka(a)
        print()
        choise = menu()
        while choise == 3:
            vyvod(a)
            print()
            choise = menu()
        else:
            break
