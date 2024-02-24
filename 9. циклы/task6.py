num_of_strings = int(input("Введите количество строк: "))
strings = []
for _ in range(num_of_strings):
    string = input("Введите строку: ")
    strings.append(string)

from collections import Counter
counter = Counter(strings)
print(*counter)
