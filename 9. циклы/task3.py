alphabet = list("abcdefghijklmnopqrstuvwxyz")
result = [letter * (index + 1) for index, letter in enumerate(alphabet)]
print(result)
