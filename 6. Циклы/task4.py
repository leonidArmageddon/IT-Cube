n = int(input("Введите количество карт: "))

# Сумма всех карт
total_sum = n * (n + 1) // 2

# Сумма оставшихся карт + проверяем условия
cards_sum = 0
for _ in range(n - 1):
    card = int(input("Номер карты: "))
    if card > 0 and card != 1:  # Проверяем на условие
        cards_sum += card

# Определяем недостающую карту
missing_card = total_sum - cards_sum if total_sum >= cards_sum else "Недостающей карты не может быть"

print(f"Недостающая карта: {missing_card}")
