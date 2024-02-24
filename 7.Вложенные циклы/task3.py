for num in range(int(input("Введите x: ")), int(input("Введите y: ")) + 1):
    if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
        print(num)
