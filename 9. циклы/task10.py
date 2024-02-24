numbers = list(map(int, input("dведите числа, разделенные пробелом: ").split()))
if len(numbers) < 2:
    print("yедостаточно чисел!")
else:
    mini, maxi = min(numbers), max(numbers)
    min_index, max_index = numbers.index(mini), numbers.index(maxi)
    numbers[min_index], numbers[max_index] = maxi, mini
    print(numbers)
