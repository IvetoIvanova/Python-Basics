first_player_eggs = int(input())
second_player_eggs = int(input())

for _ in range(100):
    winner = input()

    if winner == 'one':
        second_player_eggs -= 1
    elif winner == 'two':
        first_player_eggs -= 1

    if winner == 'End':
        print(f'Player one has {first_player_eggs} eggs left.')
        print(f'Player two has {second_player_eggs} eggs left.')
        break

    if first_player_eggs == 0:
        print(f'Player one is out of eggs. '
              f'Player two has {second_player_eggs} eggs left.')
        break
    elif second_player_eggs == 0:
        print(f'Player two is out of eggs. '
              f'Player one has {first_player_eggs} eggs left.')
        break
