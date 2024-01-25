
num = input("Введите четырехзначное число: ")
if num[0] == '-':
    sign= num[0]
    num = num[1:]
else:
    sign = ''
digits = [int(digit) for digit in str(num)]

for digit in digits:
    print(digit)
