import CheckInput
absolute_zero = -459.67
print('Программма перевода градусов по Фаренгейту в градусы по Цельсию')

F = CheckInput.getNumber('Введите значение градусов по Фаренгейту: ')

while F <= absolute_zero:
    print('Ошибка, введенное значение меньше чем '+str(absolute_zero))
    F = CheckInput.getNumber('Введите значение градусов по Фаренгейту: ')
else:
    C = float((5/9)*(float(F)-32))
    print('Пo цельсию равно: {0:.1f} '.format(C))