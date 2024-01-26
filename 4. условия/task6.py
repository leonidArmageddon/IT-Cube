x1, y1, x2, y2 = map(int, input().split())
def move(x1, y1, x2, y2):
    if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
        if x1 == x2 or y1 == y2:
            return("Да")
        else:
            return("Нет")
    else:
        return("Координаты выходят за пределы доски")

print(move(x1, y1, x2, y2))
