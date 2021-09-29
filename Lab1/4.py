import CheckInput
import math

print('Программа вычисления периметра треугольника по координатам вершин')

x1 = CheckInput.getNumber('Введите координату x1: ')
y1 = CheckInput.getNumber('Введите координату y1: ')
x2 = CheckInput.getNumber('Введите координату x2: ')
y2 = CheckInput.getNumber('Введите координату y2: ')
x3 = CheckInput.getNumber('Введите координату x3: ')
y3 = CheckInput.getNumber('Введите координату y3: ')


P = (math.sqrt((x2-x1)**2) + math.sqrt((y2-y1)**2)) + (math.sqrt((x3-x2)**2) + math.sqrt((y3-y2)**2)) + (math.sqrt((x3-x1)**2) + math.sqrt((y3-y1)**2))

print('Периметр треугольника равен: {0:.1f} '.format(P))
