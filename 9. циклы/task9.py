list = []
str_1 = input('введите строку ')
str_2 = input('введите разделитель ')
list.extend(str_1)

print(*list, sep=str_2)