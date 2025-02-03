number_of_painted_eggs = int(input())

num_of_red_eggs = 0
num_of_orange_eggs = 0
num_of_blue_eggs = 0
num_of_green_eggs = 0

for _ in range(number_of_painted_eggs):
    egg_color = input()

    if egg_color == 'red':
        num_of_red_eggs += 1
    elif egg_color == 'orange':
        num_of_orange_eggs += 1
    elif egg_color == 'blue':
        num_of_blue_eggs += 1
    elif egg_color == 'green':
        num_of_green_eggs += 1

max_eggs = num_of_red_eggs
max_color = 'red'

if num_of_orange_eggs > max_eggs:
    max_eggs = num_of_orange_eggs
    max_color = 'orange'
if num_of_blue_eggs > max_eggs:
    max_eggs = num_of_blue_eggs
    max_color = 'blue'
if num_of_green_eggs > max_eggs:
    max_eggs = num_of_green_eggs
    max_color = 'green'

print(f'Red eggs: {num_of_red_eggs}')
print(f'Orange eggs: {num_of_orange_eggs}')
print(f'Blue eggs: {num_of_blue_eggs}')
print(f'Green eggs: {num_of_green_eggs}')
print(f'Max eggs: {max_eggs} -> {max_color}')
