name1 = input("Введите первое имя: ")
name2 = input("Введите второе имя: ")
name3 = input("Введите третье имя: ")

names = [name1, name2, name3]

longest_name = max(names, key=len)
shortest_name = min(names, key=len)

print("Самое длинное имя:", longest_name)
print("Самое короткое имя:", shortest_name)
