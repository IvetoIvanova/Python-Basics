winner = ""
max_points = 0

while True:
    player_name = input()

    if player_name == "Stop":
        break

    points = 0

    for char in player_name:
        num = int(input())

        if num == ord(char):
            points += 10
        else:
            points += 2

    if points >= max_points:
        max_points = points
        winner = player_name

print(f"The winner is {winner} with {max_points} points!")
