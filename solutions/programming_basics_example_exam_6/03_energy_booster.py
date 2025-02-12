fruit = input()
set_size = input()
num_of_ordered_sets = int(input())

total_price = 0.0

if set_size == 'small':
    if fruit == 'Watermelon':
        total_price = 56
    elif fruit == 'Mango':
        total_price = 36.66
    elif fruit == 'Pineapple':
        total_price = 42.10
    elif fruit == 'Raspberry':
        total_price = 20
    total_price = total_price * 2 * num_of_ordered_sets
elif set_size == 'big':
    if fruit == 'Watermelon':
        total_price = 28.70
    elif fruit == 'Mango':
        total_price = 19.60
    elif fruit == 'Pineapple':
        total_price = 24.80
    elif fruit == 'Raspberry':
        total_price = 15.20
    total_price = total_price * 5 * num_of_ordered_sets

if 400 <= total_price <= 1000:
    total_price -= (total_price * 0.15)
elif total_price > 1000:
    total_price /= 2

print(f'{total_price:.2f} lv.')
