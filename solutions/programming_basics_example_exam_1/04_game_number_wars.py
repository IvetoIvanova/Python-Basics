first_player_name = input()
second_player_name = input()

first_player_points = 0
second_player_points = 0

while True:
    data1 = input()
    if data1 == 'End of game':
        print(f'{first_player_name} has {first_player_points} points')
        print(f'{second_player_name} has {second_player_points} points')
        break

    current_second_player_card = int(input())
    current_first_player_card = int(data1)

    if current_first_player_card > current_second_player_card:
        first_player_points += (current_first_player_card - current_second_player_card)
    elif current_second_player_card > current_first_player_card:
        second_player_points += (current_second_player_card - current_first_player_card)
    else:
        print("Number wars!")

        while True:
            next_card_1 = int(input())
            next_card_2 = int(input())
            if next_card_1 > next_card_2:
                print(f'{first_player_name} is winner with {first_player_points} points')
                break
            elif next_card_2 > next_card_1:
                print(f'{second_player_name} is winner with {second_player_points} points')
                break
        break
