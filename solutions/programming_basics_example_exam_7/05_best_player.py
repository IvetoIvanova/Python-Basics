player_with_max_goals = ''
max_goals = 0
hat_trick = False

while True:
    data = input()

    if data == 'END':
        break

    number_of_goals = int(input())

    if number_of_goals > max_goals:
        player_with_max_goals = data
        max_goals = number_of_goals
        if max_goals >= 3:
            hat_trick = True

    if number_of_goals >= 10:
        break

print(f'{player_with_max_goals} is the best player!')

if hat_trick:
    print(f'He has scored {max_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {max_goals} goals.')
