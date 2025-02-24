budget = float(input())
nights_number = int(input())
price_per_night = float(input())
overhead_percentage = int(input())

additional_costs = budget * (overhead_percentage / 100)

if nights_number > 7:
    price_per_night *= 0.95

total_sum = (nights_number * price_per_night) + additional_costs
money_left = abs(budget - total_sum)

if budget >= total_sum:
    print(f'Ivanovi will be left with {money_left:.2f} leva after vacation.')
else:
    print(f'{money_left:.2f} leva needed.')
