import random

try:
    with open("words.txt", "r", encoding="utf-8") as file:
        words = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print("Error: words.txt not found! Please create the file and add words.")
    exit()

if not words:
    print("Error: words.txt is empty! Please add some words.")
    exit()

easy_words = []
medium_words = []
hard_words = []

for w in words:
    if len(w) <= 5:
        easy_words.append(w)
    elif 6 <= len(w) <= 8:
        medium_words.append(w)
    else:
        hard_words.append(w)

print("\nChoose a difficulty level:")
print("1 - Easy (short words)")
print("2 - Medium (medium-length words)")
print("3 - Hard (long words)")
difficulty = input("Enter 1, 2, or 3: ").strip()

if difficulty == "1":
    selected_words = easy_words
elif difficulty == "2":
    selected_words = medium_words
elif difficulty == "3":
    selected_words = hard_words
else:
    print("Invalid choice! Defaulting to Medium difficulty.")
    selected_words = medium_words

if not selected_words:
    print("Error: No words available for this difficulty level.")
    exit()


def play_turn(player_name, words_pool):
    if not words_pool:
        print(f"\nNo more words left! {player_name} can't play this round.")
        return 0

    word = random.choice(words_pool)
    words_pool.remove(word)
    scrambled = list(word)
    random.shuffle(scrambled)
    scrambled = "".join(scrambled)

    print(f"\n{player_name}, it's your turn!")
    print(f"Scrambled word: {scrambled}")

    attempts = 3
    for i in range(attempts):
        guess = input(f"Attempt {i + 1}/{attempts} - Unscramble the word (or type 'end' to stop): ").strip().lower()

        if guess == "end":
            print(f"{player_name} chose to end the game.")
            return "end"

        if guess == word.lower():
            print(f"{player_name} guessed the word correctly!")
            return 1
        else:
            print(f"Wrong answer! You have {attempts - (i + 1)} attempts left.")

    print(f"Game over! The correct word was '{word}'.")
    return 0


print("\nWelcome to 'Unscramble it!'")
mode = input("Do you want to play Singleplayer (1) or Multiplayer (2)? ").strip()

if mode == "2":
    print("\nMultiplayer mode selected!")
    player1 = input("Enter Player 1 name: ").strip()
    player2 = input("Enter Player 2 name: ").strip()

    print(f"\n{player1} vs {player2} - Let’s see who unscrambles more words! 🚀")

    score1, score2 = 0, 0
    words_left = selected_words.copy()

    while words_left:
        result = play_turn(player1, words_left)
        if result == "end":
            break
        score1 += result

        if not words_left:
            break

        result = play_turn(player2, words_left)
        if result == "end":
            break
        score2 += result

        print(f"\nCurrent Score: {player1} - {score1} | {player2} - {score2}")
        print("-" * 40)

    print("\nFinal Score:")
    print(f"{player1}: {score1} points")
    print(f"{player2}: {score2} points")

    if score1 > score2:
        print(f"🏆 {player1} wins!")
    elif score2 > score1:
        print(f"🏆 {player2} wins!")
    else:
        print("It's a tie!")

else:
    print("\nSingleplayer mode selected!")
    player_score = 0
    words_left = selected_words.copy()

    while words_left:
        result = play_turn("Player", words_left)
        if result == "end":
            break
        player_score += result

        print(f"\nYour Score: {player_score}")
        print("-" * 40)

    print(f"\nGame over! Final Score: {player_score} points.")

if not words_left:
    print("\nNo more words left! If you want to play more rounds, add new words to 'words.txt'.")
