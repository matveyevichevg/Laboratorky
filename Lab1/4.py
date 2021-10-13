import CheckInput
import math

print('Программа вычисления периметра треугольника по координатам вершин')

#Ввод координат вершин треугольника
print('Введите координаты точки А вашего треугольника: ')
a = CheckInput.getCoordinate()
print('Введите координаты точки B вашего треугольника: ')
b = CheckInput.getCoordinate()
print('Введите координаты точки C вашего треугольника: ')
c = CheckInput.getCoordinate()

#Вычисление длин сторон треугольника, периметра и вывод ответа
perimeter = math.sqrt(((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2)) + math.sqrt(((c[0] - b[0]) ** 2) + ((c[1] - b[1]) ** 2)) + math.sqrt(((c[0] - a[0]) ** 2) + ((c[1] - a[1]) ** 2))
print('Периметр треугольника равен: {0:.1f}'.format(perimeter))