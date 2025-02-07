strawberries_price_per_kg = float(input())
kilograms_of_bananas = float(input())
kilograms_of_oranges = float(input())
kilograms_of_raspberries = float(input())
kilograms_of_strawberries = float(input())

raspberries_price_per_kg = strawberries_price_per_kg / 2
orange_price_per_kg = raspberries_price_per_kg * 0.60
bananas_price_per_kg = raspberries_price_per_kg * 0.20

strawberries_total_price = kilograms_of_strawberries * strawberries_price_per_kg
raspberries_total_price = kilograms_of_raspberries * raspberries_price_per_kg
orange_total_price = kilograms_of_oranges * orange_price_per_kg
bananas_total_price = kilograms_of_bananas * bananas_price_per_kg

needed_money = strawberries_total_price + raspberries_total_price + orange_total_price + bananas_total_price

print(f'{needed_money:.2f}')
