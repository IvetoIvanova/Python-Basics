days = int(input())
total_money = 0
days_won = 0

for day in range(days):
    wins = 0
    losses = 0
    daily_money = 0

    while True:
        game = input()

        if game == "Finish":
            break

        result = input()

        if result == "win":
            wins += 1
            daily_money += 20
        else:
            losses += 1

    if wins > losses:
        daily_money *= 1.10
        days_won += 1

    total_money += daily_money

if days_won > days / 2:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
