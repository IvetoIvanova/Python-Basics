purchased_food_kg = int(input())

purchased_food_g = purchased_food_kg * 1000
total_food_in_g = 0

while True:
    data = input()

    if data == 'Adopted':
        break

    food_for_meal_g = int(data)

    total_food_in_g += food_for_meal_g

if purchased_food_g >= total_food_in_g:
    leftover_food = purchased_food_g - total_food_in_g
    print(f'Food is enough! Leftovers: {leftover_food} grams.')
else:
    needed_food = total_food_in_g - purchased_food_g
    print(f'Food is not enough. You need {needed_food} grams more.')
