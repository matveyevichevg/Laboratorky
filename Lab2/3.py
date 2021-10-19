# В одномерном массиве целых чисел заменить максимальное значение минималь-ным.
import CheckInput
import numpy as np

def vvod():
    array = CheckInput.arrayInput_int()
    return array

#Замена максимального значения на минимальное
def obrabotka(array):
    #Поиск индекса максимального значения
    maxArgument = np.argmax(array)
    #Поиск  минимального значения
    minArgument = np.amin(array)
    #Замена максимального значения - минимальным
    array[maxArgument] = minArgument

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
        obrabotka(a)
        print('Массив обработан')
        print()
        choise = CheckInput.menu()
    elif choise == 3:
        vyvod(a)
        print()
        choise = CheckInput.menu()
    elif choise == 4:
        quit()
