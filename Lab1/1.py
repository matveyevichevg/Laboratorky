import math
import CheckInput

print('Программа для вычисления гипотенузы треугольника')

a=CheckInput.getPositiveNumber('Введите катет а:')
b=CheckInput.getPositiveNumber('Введите катет b:')

gip = math.sqrt(a**2 + b**2)
print('Гипотенуза равна: {0:.1f} '.format(gip))


