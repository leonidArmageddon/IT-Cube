num_of_strings = int(input("введите количество строк: "))
strings = []
for _ in range(num_of_strings):
    string = input("введите строку: ")
    strings.append(string)

num_to_find = int(input("Введите номер буквы "))

for string in strings:
    if num_to_find <= len(string) and num_to_find > 0:
        print(string[num_to_find - 1], end='')
    else:
        print(f"В слове '{string}' меньше {num_to_find} букв")
