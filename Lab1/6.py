import CheckInput

print('Программа для определения силы притяжения между двумя телами')

m1 = CheckInput.getPositiveNumber('Введите массу первого тела: ')
m2 = CheckInput.getPositiveNumber('Введите массу второго тела: ')
r = CheckInput.getPositiveNumber('Введите расстояние между телами: ')
const_G=6.67*(10**-11)

F=const_G*((m1*m2)/(r**2))
print('Сила притяжения равна: ' + str(F))
