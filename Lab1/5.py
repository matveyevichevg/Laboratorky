import CheckInput

print('Прогрмма определяет сколько полных часов и минут прошло к заданному в секундах времени')

second = CheckInput.getPositiveNumber('Введите, секунду суток: ')
SECONDS_IN_DAY = 86400
MINUTE_IN_SECONDS = 60
HOUR_IN_SECONDS = 3600
while second > SECONDS_IN_DAY:
    print('Ошибка, заданное значение больше, чем количество секунд в сутках')
    second = CheckInput.getPositiveNumber('Введите, секунду суток: ')
else:
    hour = second / HOUR_IN_SECONDS
    minute = second / MINUTE_IN_SECONDS
    print('Полных часов: {0:.0f}'.format(hour))
    print('Полных минут: {0:.0f}'.format(minute))