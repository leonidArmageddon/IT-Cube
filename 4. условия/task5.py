# ЗАДАНИЕ 5

a = int(input('Введите число '))
if a > 999 and a % 7 == 0 or a % 17 == 0:
    print('Красивое!')
else:
    print('Страшное!')