import CheckInput

print('Прогрмма определяет сколько полных часов и минут прошло к заданному в секундах времени')

second = CheckInput.getPositiveNumber('Введите, секунду суток: ')

if second > 86400:
    print('Ошибка, заданное значение больше, чем количество секунд в сутках')
    second = CheckInput.getPositiveNumber('Введите, секунду суток: ')
else:
    hour = second/3600
    minute = second/60
    print('Полных часов: {0:.0f}  '.format(hour))
    print('Полных минут: {0:.0f}  '.format(minute))