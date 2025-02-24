town_name = input()
package_type = input()
vip_discount = input()
days_to_stay = int(input())

price_per_day = 0
discount = 0
invalid_input = False

if town_name == 'Bansko' or town_name == 'Borovets':
    if package_type == 'noEquipment':
        price_per_day = 80
        discount = 0.05
    elif package_type == 'withEquipment':
        price_per_day = 100
        discount = 0.10
    else:
        invalid_input = True
elif town_name == 'Varna' or town_name == 'Burgas':
    if package_type == 'noBreakfast':
        price_per_day = 100
        discount = 0.07
    elif package_type == 'withBreakfast':
        price_per_day = 130
        discount = 0.12
    else:
        invalid_input = True
else:
    invalid_input = True

if vip_discount == 'yes':
    price_per_day -= price_per_day * discount

total_sum = days_to_stay * price_per_day

if days_to_stay > 7:
    total_sum -= price_per_day

if days_to_stay < 1:
    print('Days must be positive number!')
elif invalid_input:
    print('Invalid input!')
else:
    print(f'The price is {total_sum:.2f}lv! Have a nice time!')
