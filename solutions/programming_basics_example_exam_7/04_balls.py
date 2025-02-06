import math

number_of_balls = int(input())

red_ball_counter = 0
orange_ball_counter = 0
yellow_ball_counter = 0
white_ball_counter = 0
black_ball_counter = 0
other_colors_picked = 0
points = 0

for _ in range(number_of_balls):
    ball_color = input()

    if ball_color == 'red':
        points += 5
        red_ball_counter += 1
    elif ball_color == 'orange':
        points += 10
        orange_ball_counter += 1
    elif ball_color == 'yellow':
        points += 15
        yellow_ball_counter += 1
    elif ball_color == 'white':
        points += 20
        white_ball_counter += 1
    elif ball_color == 'black':
        points = math.floor(points / 2)
        black_ball_counter += 1
    else:
        other_colors_picked += 1
        continue

print(f'Total points: {points}')
print(f'Red balls: {red_ball_counter}')
print(f'Orange balls: {orange_ball_counter}')
print(f'Yellow balls: {yellow_ball_counter}')
print(f'White balls: {white_ball_counter}')
print(f'Other colors picked: {other_colors_picked}')
print(f'Divides from black balls: {black_ball_counter}')
