num_of_strings = int(input("введите количество строк: "))
strings = []
for _ in range(num_of_strings):
    string = input("введите строку: ")
    strings.append(string)

word = input('введите слово ')
for i in strings:
    if word in i:
        print(i)
    