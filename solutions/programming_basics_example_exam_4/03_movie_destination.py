budget = float(input())
destination = input()
season = input()
days_number = int(input())

total_price = 0

if season == 'Summer':
    if destination == 'Dubai':
        total_price = 40_000
    elif destination == 'Sofia':
        total_price = 12_500
    elif destination == 'London':
        total_price = 20_250
elif season == 'Winter':
    if destination == 'Dubai':
        total_price = 45_000
    elif destination == 'Sofia':
        total_price = 17_000
    elif destination == 'London':
        total_price = 24_000

total_price *= days_number

if destination == 'Dubai':
    total_price *= 0.70
elif destination == 'Sofia':
    total_price *= 1.25

money = abs(budget - total_price)
if budget >= total_price:
    # budget_left = budget - total_price
    print(f'The budget for the movie is enough! We have {money:.2f} leva left!')
else:
    # needed_money = total_price - budget
    print(f'The director needs {money:.2f} leva more!')
