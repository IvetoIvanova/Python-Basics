import math

wall_height = int(input())
wall_width = int(input())
percentage_not_painted = int(input())

total_area = wall_height * wall_width * 4
total_area_for_painted = total_area - (total_area * percentage_not_painted / 100)
total_area_for_painted = math.ceil(total_area_for_painted)
is_tired = False

while True:
    data = input()

    if data == 'Tired!':
        is_tired = True
        break

    paint_liters = int(data)

    total_area_for_painted -= paint_liters

    if total_area_for_painted <= 0:
        break

if is_tired:
    print(f'{total_area_for_painted} quadratic m left.')

if total_area_for_painted < 0:
    print(f'All walls are painted and you have {abs(total_area_for_painted)} l paint left!')
elif total_area_for_painted == 0:
    print('All walls are painted! Great job, Pesho!')
