flour_price_per_kg = float(input())
kgs_of_flour = float(input())
kgs_of_sugar = float(input())
number_of_egg_cartons = int(input())
packets_of_yeast = int(input())

sugar_price_per_kg = flour_price_per_kg * 0.75
price_per_dozen_egg_carton = flour_price_per_kg * 1.10
price_per_pack_of_yeast = sugar_price_per_kg * 0.20

needed_sum = ((kgs_of_flour * flour_price_per_kg)
              + (kgs_of_sugar * sugar_price_per_kg)
              + (number_of_egg_cartons * price_per_dozen_egg_carton)
              + (packets_of_yeast * price_per_pack_of_yeast))

print(f'{needed_sum:.2f}')
