num = int(input("Введите число: "))
if num <= 0:
        print("Пожалуйста, введите положительное число.")
else:
    for i in range(1, num+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
               count += 1
        print(f'{i} - {count}')
