drink = input()
sugar = input()
drinks_number = int(input())

drink_price = 0

if drink == 'Espresso':
    if sugar == 'Without':
        drink_price = 0.90
    elif sugar == 'Normal':
        drink_price = 1
    elif sugar == 'Extra':
        drink_price = 1.20
elif drink == 'Cappuccino':
    if sugar == 'Without':
        drink_price = 1.00
    elif sugar == 'Normal':
        drink_price = 1.20
    elif sugar == 'Extra':
        drink_price = 1.60
elif drink == 'Tea':
    if sugar == 'Without':
        drink_price = 0.50
    elif sugar == 'Normal':
        drink_price = 0.60
    elif sugar == 'Extra':
        drink_price = 0.70

total_sum = drink_price * drinks_number

if sugar == 'Without':
    total_sum -= total_sum * 0.35

if drink == 'Espresso' and drinks_number >= 5:
    total_sum -= total_sum * 0.25

if total_sum > 15:
    total_sum -= total_sum * 0.20

print(f'You bought {drinks_number} cups of {drink} for {total_sum:.2f} lv.')
