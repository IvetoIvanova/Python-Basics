import math

num_of_tournaments = int(input())
initial_points = int(input())

total_points_from_tournaments = 0
win_counter = 0

for _ in range(num_of_tournaments):
    tournament_stage_reached = input()

    if tournament_stage_reached == 'W':
        total_points_from_tournaments += 2000
        win_counter += 1
    elif tournament_stage_reached == 'F':
        total_points_from_tournaments += 1200
    elif tournament_stage_reached == 'SF':
        total_points_from_tournaments += 720

average_points = math.floor(total_points_from_tournaments / num_of_tournaments)
percent_of_tournaments_won = win_counter / num_of_tournaments * 100

print(f'Final points: {total_points_from_tournaments + initial_points}')
print(f'Average points: {average_points}')
print(f'{percent_of_tournaments_won:.2f}%')
