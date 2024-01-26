# ЗАДАНИЕ 3

n = int(input('Введите числа без пробелов '))
result = []
while n != 0:
    n, d = divmod(n, 10)
    result.append(int(d))
result.reverse()
print(min(result))
