import math

number_of_people = int(input())
entrance_fee = float(input())
price_per_sun_lounger = float(input())
price_per_umbrella = float(input())

total_entrance_fee = number_of_people * entrance_fee
total_sun_lounger = math.ceil(number_of_people * 0.75) * price_per_sun_lounger
total_umbrellas = math.ceil(number_of_people / 2) * price_per_umbrella

total_sum = total_entrance_fee + total_sun_lounger + total_umbrellas

print(f'{total_sum:.2f} lv.')
