N = int(input())
maxDigit = -1

while N > 0:
    digit = N % 10
    if digit % 2 == 0 and digit > maxDigit:
        maxDigit = digit
    N = N // 10

if maxDigit == -1:
    print('Нет числоа кратного 2')
else:
    print(maxDigit)
    