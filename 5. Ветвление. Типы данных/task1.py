n = int(input("Введите количество собачьих лет: "))

def dog_age_converter(n):
    if n <= 2:
        human_years = n * 10.5
    else:
        human_years = 2 * 10.5 + (n - 2) * 4
    return human_years

result = dog_age_converter(n)
print(f"Возраст собаки в человеческих годах: {result}")
