bits_number = int(input())
number_of_egg_cartons = int(input())
cookies_in_kg = int(input())

bits_total_price = bits_number * 3.20
egg_cartons_total_price = number_of_egg_cartons * 4.35
cookies_total_price = cookies_in_kg * 5.40
egg_dye_price = (number_of_egg_cartons * 12) * 0.15

total_sum = (bits_total_price
             + egg_cartons_total_price
             + cookies_total_price
             + egg_dye_price)

print(f'{total_sum:.2f}')
