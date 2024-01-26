# ЗАДАНИЕ 5
number = int(input("Введите число: "))
if len(str(number)) == 4 and (number % 7 == 0 or number % 17 == 0):
    print("Красивое")
else:
    print("Страшное")
