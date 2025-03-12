desired_height = int(input())

current_height = desired_height - 30
total_jumps = 0
failed_attempts = 0
failed = False

while current_height <= desired_height:
    for _ in range(3):
        jump_height = int(input())
        total_jumps += 1

        if jump_height > current_height:
            current_height += 5
            failed_attempts = 0
            break
        else:
            failed_attempts += 1

        if failed_attempts == 3:
            failed = True
            break

    if failed:
        break

if failed:
    print(f"Tihomir failed at {current_height}cm after {total_jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {current_height - 5}cm after {total_jumps} jumps.")
