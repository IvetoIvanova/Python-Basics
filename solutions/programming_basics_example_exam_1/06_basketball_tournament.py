total_games = 0
win_count = 0
lose_count = 0

while True:
    tournament_name = input()

    if tournament_name == "End of tournaments":
        break

    matches_count = int(input())

    for match_number in range(1, matches_count + 1):
        desi_points = int(input())
        opponent_points = int(input())
        total_games += 1

        if desi_points > opponent_points:
            win_count += 1
            print(f"Game {match_number} of tournament "
                  f"{tournament_name}: win with {desi_points - opponent_points} points.")
        else:
            lose_count += 1
            print(f"Game {match_number} of tournament "
                  f"{tournament_name}: lost with {opponent_points - desi_points} points.")

win_percentage = (win_count / total_games) * 100
lose_percentage = (lose_count / total_games) * 100

print(f"{win_percentage:.2f}% matches win")
print(f"{lose_percentage:.2f}% matches lost")
