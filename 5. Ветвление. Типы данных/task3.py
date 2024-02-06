number = int(input("Введите трехзначное число: "))

digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

min_digit = min(digit1, digit2, digit3)
max_digit = max(digit1, digit2, digit3)
median_digit = digit1 + digit2 + digit3 - min_digit - max_digit

if max_digit - min_digit == median_digit:
    print("Прикольное")
else:
    print("Не прикольное")
