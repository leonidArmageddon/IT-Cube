import cmath
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

#дискриминант
D = b**2 - 4*a*c

#проверка дискриминанта
if D > 0:
    x1 = (-b + cmath.sqrt(D)) / (2 * a)
    x2 = (-b - cmath.sqrt(D)) / (2 * a)
    print("У уравнения два вещественных корня:", x1, "и", x2)
elif D == 0:
    x = -b / (2 * a)
    print("У уравнения один вещественный корень:", x)
else:
    real_part = -b / (2 * a)
    imag_part = cmath.sqrt(-D) / (2 * a)
    print("У уравнения два комплексных корня:", real_part, "+", imag_part, "и", real_part, "-", imag_part)
