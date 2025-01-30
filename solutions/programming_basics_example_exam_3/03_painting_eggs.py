egg_size = input()
egg_color = input()
num_of_lots = int(input())

# production_costs
sum_without_production_costs = 0.0

if egg_size == 'Large':
    if egg_color == 'Red':
        sum_without_production_costs = num_of_lots * 16
    elif egg_color == 'Green':
        sum_without_production_costs = num_of_lots * 12
    elif egg_color == 'Yellow':
        sum_without_production_costs = num_of_lots * 9
elif egg_size == 'Medium':
    if egg_color == 'Red':
        sum_without_production_costs = num_of_lots * 13
    elif egg_color == 'Green':
        sum_without_production_costs = num_of_lots * 9
    elif egg_color == 'Yellow':
        sum_without_production_costs = num_of_lots * 7
elif egg_size == 'Small':
    if egg_color == 'Red':
        sum_without_production_costs = num_of_lots * 9
    elif egg_color == 'Green':
        sum_without_production_costs = num_of_lots * 8
    elif egg_color == 'Yellow':
        sum_without_production_costs = num_of_lots * 5

production_costs = sum_without_production_costs * 0.35
total_sum = sum_without_production_costs - production_costs

print(f'{total_sum:.2f} leva.')
