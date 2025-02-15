days = int(input())
total_food_quantity = float(input())

total_biscuits = 0
total_food_eaten = 0
total_food_dog_eaten = 0
total_food_cat_eaten = 0

for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())

    total_food_eaten += dog_food + cat_food

    if day % 3 == 0:
        total_biscuits += (dog_food + cat_food) * 0.1

    total_food_dog_eaten += dog_food
    total_food_cat_eaten += cat_food

percent_cookies = round(total_biscuits)
percent_food_eaten = (total_food_eaten / total_food_quantity) * 100
percent_food_dog_eaten = (total_food_dog_eaten / total_food_eaten) * 100
percent_food_cat_eaten = (total_food_cat_eaten / total_food_eaten) * 100

print(f'Total eaten biscuits: {percent_cookies}gr.')
print(f'{percent_food_eaten:.2f}% of the food has been eaten.')
print(f'{percent_food_dog_eaten:.2f}% eaten from the dog.')
print(f'{percent_food_cat_eaten:.2f}% eaten from the cat.')
