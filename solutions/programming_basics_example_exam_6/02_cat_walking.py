minutes_of_walking_per_day = int(input())
number_of_walks_per_day = int(input())
calories_received_per_day = int(input())

total_minutes_walking = minutes_of_walking_per_day * number_of_walks_per_day
total_calories_burned_per_day = total_minutes_walking * 5
enough_walk = calories_received_per_day * 0.50

if total_calories_burned_per_day >= enough_walk:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {total_calories_burned_per_day}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {total_calories_burned_per_day}.')
