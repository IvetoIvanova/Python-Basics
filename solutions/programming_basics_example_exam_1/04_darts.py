player_name = input()
player_points = 301

unsuccessful_shots = 0
successful_shots = 0
field_points = 0

while player_points > 0:
    data = input()

    if data == 'Retire':
        print(f'{player_name} retired after {unsuccessful_shots} unsuccessful shots.')
        break

    current_points = int(input())

    if data == 'Single':
        field_points = current_points
    elif data == 'Double':
        field_points = 2 * current_points
    elif data == 'Triple':
        field_points = 3 * current_points

    if field_points > player_points:
        unsuccessful_shots += 1
        continue
    else:
        player_points -= field_points
        successful_shots += 1

else:
    print(f'{player_name} won the leg with {successful_shots} shots.')
