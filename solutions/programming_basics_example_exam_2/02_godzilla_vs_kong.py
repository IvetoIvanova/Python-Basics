film_budget = float(input())
number_of_extras = int(input())
price_per_clothing = float(input())

decor_amount = film_budget * 0.10

if number_of_extras > 150:
    price_per_clothing = price_per_clothing * 0.90

total_sum = (number_of_extras * price_per_clothing) + decor_amount

if total_sum > film_budget:
    money_lacking = total_sum - film_budget
    print('Not enough money!')
    print(f'Wingard needs {money_lacking:.2f} leva more.')
else:
    money_left = film_budget - total_sum
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
