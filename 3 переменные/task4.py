import itertools
num = input("Введите трехзначное число: ")
if num[0] == '-':
    sign= num[0]
    num = num[1:]
else:
    sign = ''
permutations = list(itertools.permutations(num))
for permutation in permutations:
    print(''.join(permutation))
