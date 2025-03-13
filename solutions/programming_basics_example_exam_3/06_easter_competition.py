breads_count = int(input())

best_baker = ""
best_score = 0

for _ in range(breads_count):
    baker_name = input()
    total_points = 0

    while True:
        score = input()

        if score == "Stop":
            break

        total_points += int(score)

    print(f"{baker_name} has {total_points} points.")

    if total_points > best_score:
        best_score = total_points
        best_baker = baker_name
        print(f"{baker_name} is the new number 1!")

print(f"{best_baker} won competition with {best_score} points!")
