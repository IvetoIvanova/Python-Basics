number_games = int(input())

hearthstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
others_counter = 0
sales_percentage = 0

for _ in range(number_games):
    game_name = input()

    if game_name == 'Hearthstone':
        hearthstone_counter += 1
    elif game_name == 'Fornite':
        fornite_counter += 1
    elif game_name == 'Overwatch':
        overwatch_counter += 1
    else:
        others_counter += 1

hearthstone_sales_percentage = hearthstone_counter / number_games * 100
fornite_sales_percentage = fornite_counter / number_games * 100
overwatch_sales_percentage = overwatch_counter / number_games * 100
others_sales_percentage = others_counter / number_games * 100

print(f'Hearthstone - {hearthstone_sales_percentage:.2f}%')
print(f'Fornite - {fornite_sales_percentage:.2f}%')
print(f'Overwatch - {overwatch_sales_percentage:.2f}%')
print(f'Others - {others_sales_percentage:.2f}%')
