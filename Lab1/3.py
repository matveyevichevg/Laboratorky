def ex(f):
    try:
        if int(f):
            return True
        else:
            return False
    except ValueError:
        return False
while True:
    F = input('Введите градусы по фаренгейту: ')
    if ex(F):
        F=float(F)
        break
    else:
        print('Ошибка, ведите число')

C = (5/9)*(int(F)-32)
print('По цельсию равно ', int(C))