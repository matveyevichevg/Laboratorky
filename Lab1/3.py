import CheckInput
ABSOLUTE_ZERO_FAHR = -459.67
print('Программма перевода градусов по Фаренгейту в градусы по Цельсию')

fahr = CheckInput.getNumber('Введите значение градусов по Фаренгейту: ')

while fahr <= ABSOLUTE_ZERO_FAHR:
    print('Ошибка, введенное значение меньше чем {0:.1f}'.format(ABSOLUTE_ZERO_FAHR) )
    fahr = CheckInput.getNumber('Введите значение градусов по Фаренгейту: ')
else:
    cel = float((5/9) * (float(fahr) - 32))
    print('Пo цельсию равно: {0:.1f} '.format(cel))