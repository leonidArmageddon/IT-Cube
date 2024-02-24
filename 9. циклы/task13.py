numbers_str = input("введите целые числа, разделенные пробелом: ")
numbers = list(map(int, numbers_str.split()))

result = [num ** 2 for num in numbers if num % 2 == 0 and num % 10 != 4]

print(result)
