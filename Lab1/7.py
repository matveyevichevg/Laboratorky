import CheckInput
import math

#Идентификация треугольника по двум сторонам и углу между ними.
# Определить, является ли треугольник равносторонним, равнобедренным или прямоугольным (второе и третье может быть одновременно).

print('Программа идентификации треугольника по двум сторонам и углу между ними')

a = CheckInput.getPositiveNumber('Введите первую сторону треугольника: ')
b = CheckInput.getPositiveNumber('Введите вторую сторону треугольника: ')
u = CheckInput.getPositiveNumber('Введите угол между сторонами треугольника: ')

while u > 180:
    print('Ошибка, угол не может быть больше 180 градусов')
    u = CheckInput.getPositiveNumber('Введите угол между сторонами треугольника: ')
else:
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(u))
print('Стороны треугольника a = {0:.1f} '.format(a), 'b = {0:.1f} '.format(b), 'c =  {0:.1f} '.format(c), 'Угол =  {0:.1f} '.format(u))
if a == b and b == c:
    print('Треугольник равносторонний')
elif u == 90 and a == b or a == c or b == c:
    print('Треугольник равнобедренный и прямоугольный')
elif a == b or a == c or b == c:
    print('Треугольник равнобедренный')
elif a != b and a != c and b != c and u == 90:
    print('Треугольник разносторонний и прямоугольный')
elif a != b and a != c and b != c:
    print('Треугольник разносторонний')


