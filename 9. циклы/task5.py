num_of_strings = int(input("введите количество строк: "))
strings = []
for _ in range(num_of_strings):
    string = input("введите строку: ")
    strings.extend(string)
print(strings)