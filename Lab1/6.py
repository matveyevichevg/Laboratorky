import CheckInput

print('Программа для определения силы притяжения между двумя телами')

m1 = CheckInput.getPositiveNumber('Введите массу первого тела в килотоннах: ')
m2 = CheckInput.getPositiveNumber('Введите массу второго тела в килотоннах: ')
r = CheckInput.getPositiveNumber('Введите расстояние между телами: ')
СONST_G = 6.67 * (10 ** -11)

F = СONST_G * ((m1 * 10 ** 6 * m2 * 10 ** 6) / (r ** 2))

print('Сила притяжения равна: {0:.1f} '.format(F))
