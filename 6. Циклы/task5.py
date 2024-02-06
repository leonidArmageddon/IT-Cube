numbers = []

while True:
    user_input = input("Введите число ('СТОП' чтобы завершить): ")

    if user_input == "СТОП":
        break
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Пожалуйста, введите целое число или 'СТОП' для завершения.")
if numbers:
    top_3 = sorted(numbers, reverse=True)[:3]
    print("Топ-3 самых больших чисел:", top_3)
else:
    print("Вы не ввели чисел.")

