from random import *
rnd = randrange(1,100)
n = int(input('Введите вашу догадку, число от 1 до 99:'))

while n != rnd:
    if n > rnd:
        n = int(input('Много, попробуйте еще!'))
    elif n < rnd:
        n = int(input('Мало, попробуйте еще!'))
    else:
        break
print(f'Отлично, Вы угадали число!\n И им было - {rnd}')
