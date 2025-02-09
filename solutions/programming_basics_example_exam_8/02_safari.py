budget = float(input())
needed_liters_of_fuel = float(input())
day_of_week = input()

total_price = (needed_liters_of_fuel * 2.10) + 100

if day_of_week == 'Saturday':
    total_price = total_price * 0.90
elif day_of_week == 'Sunday':
    total_price = total_price * 0.80

if budget >= total_price:
    money_left = budget - total_price
    print(f'Safari time! Money left: {money_left:.2f} lv.')
else:
    needed_money = total_price - budget
    print(f'Not enough money! Money needed: {needed_money:.2f} lv.')
