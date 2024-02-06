def calculator():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operation = input("Введите операцию (+, -, *, /, //, **): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("На ноль делить нельзя")
            return
        else:
            result = num1 / num2
    elif operation == '//':
        if num2 == 0:
            print("На ноль делить нельзя")
            return
        else:
            result = num1 // num2
    elif operation == '**':
        result = num1 ** num2
    else:
        print("Неподдерживаемая операция")
        return

    print("Результат:", result)

calculator()
