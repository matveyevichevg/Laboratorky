# Вариант 1
# В одномерном массиве целых чисел заменить минимальное значение средним арифметическим его элементов, находящихся на четных позициях.
import CheckInput
import numpy as np

#Ввод элементов массива
def vvod():
    array = CheckInput.arrayInput_int()
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


#Реализация меню
choise = CheckInput.menu()
a = []
while choise == 2 or choise == 3:
    print('Сначала введи массив(п.1)\n')
    choise = CheckInput.menu()
while choise:
    if choise == 1:
        a = vvod()
        print()
        choise = CheckInput.menu()
    elif choise == 2:
        obrabortka(a)
        print('Массив обработан')
        print()
        choise = CheckInput.menu()
    elif choise == 3:
        vyvod(a)
        print()
        choise = CheckInput.menu()
    elif choise == 4:
        quit()

