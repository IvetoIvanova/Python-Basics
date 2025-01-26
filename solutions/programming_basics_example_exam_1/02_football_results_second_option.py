wins = 0
losses = 0
draws = 0

for _ in range(3):
    match_result = input()

    home_goals = int(match_result.split(':')[0])
    other_team_goals = int(match_result.split(':')[1])

    if home_goals > other_team_goals:
        wins += 1
    elif home_goals < other_team_goals:
        losses += 1
    else:
        draws += 1

print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {draws}")
