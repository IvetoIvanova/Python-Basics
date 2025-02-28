team_name = input()
matches_number = int(input())

if matches_number == 0:
    print(f'{team_name} hasn\'t played any games during this season.')
elif matches_number > 0:
    total_points = 0
    w_counter = 0
    d_counter = 0
    l_counter = 0

    for _ in range(matches_number):
        result = input()

        if result == 'W':
            total_points += 3
            w_counter += 1
        elif result == 'D':
            total_points += 1
            d_counter += 1
        elif result == 'L':
            l_counter += 1

    win_rate = (w_counter / matches_number) * 100

    print(f'{team_name} has won {total_points} points during this season.')
    print('Total stats:')
    print(f'## W: {w_counter}')
    print(f'## D: {d_counter}')
    print(f'## L: {l_counter}')
    print(f'Win rate: {win_rate:.2f}%')
