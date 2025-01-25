match1_result = input()
match2_result = input()
match3_result = input()

wins = 0
losses = 0
draws = 0

home_goals = int(match1_result.split(':')[0])
other_team_goals = int(match1_result.split(':')[1])
if home_goals > other_team_goals:
    wins += 1
elif home_goals < other_team_goals:
    losses += 1
else:
    draws += 1

home_goals = int(match2_result.split(':')[0])
other_team_goals = int(match2_result.split(':')[1])
if home_goals > other_team_goals:
    wins += 1
elif home_goals < other_team_goals:
    losses += 1
else:
    draws += 1

home_goals = int(match3_result.split(':')[0])
other_team_goals = int(match3_result.split(':')[1])
if home_goals > other_team_goals:
    wins += 1
elif home_goals < other_team_goals:
    losses += 1
else:
    draws += 1

print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {draws}")
