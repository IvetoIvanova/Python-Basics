budget = float(input())
number_of_series = int(input())

total_price_of_series = 0

for _ in range(number_of_series):
    series_name = input()
    price_per_series = float(input())

    if series_name == 'Thrones':
        price_per_series /= 2
    elif series_name == 'Lucifer':
        price_per_series *= 0.60
    elif series_name == 'Protector':
        price_per_series *= 0.70
    elif series_name == 'TotalDrama':
        price_per_series *= 0.80
    elif series_name == 'Area':
        price_per_series *= 0.90

    total_price_of_series += price_per_series

if budget >= total_price_of_series:
    money_left = budget - total_price_of_series
    print(f'You bought all the series and left with {money_left:.2f} lv.')
else:
    needed_money = total_price_of_series - budget
    print(f'You need {needed_money:.2f} lv. more to buy the series!')
