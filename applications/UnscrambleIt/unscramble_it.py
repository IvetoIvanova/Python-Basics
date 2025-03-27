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


def play_turn(player_name):
    word = random.choice(selected_words)
    scrambled = list(word)
    random.shuffle(scrambled)
    scrambled = "".join(scrambled)

    print(f"\n{player_name}, it's your turn!")
    print(f"Scrambled word: {scrambled}")

    attempts = 3
    for i in range(attempts):
        guess = input(f"Attempt {i + 1}/{attempts} - Unscramble the word: ").strip().lower()
        if guess == word.lower():
            print(f"{player_name} guessed the word correctly!")
            return True
        else:
            print(f"Wrong answer! You have {attempts - (i + 1)} attempts left.")

    print(f"Game over! The correct word was '{word}'.")
    return False


print("\nWelcome to 'Unscramble it!'")
mode = input("Do you want to play Singleplayer (1) or Multiplayer (2)? ").strip()

if mode == "2":
    print("\nMultiplayer mode selected!")
    player1 = input("Enter Player 1 name: ").strip()
    player2 = input("Enter Player 2 name: ").strip()

    print(f"\n{player1} vs {player2} - Let’s see who unscrambles more words! 🚀")

    score1 = play_turn(player1)
    score2 = play_turn(player2)

    if score1 and score2:
        print("\nIt's a tie! Both players guessed their words correctly!")
    elif score1:
        print(f"\n🏆 {player1} wins!")
    elif score2:
        print(f"\n🏆 {player2} wins!")
    else:
        print("\nNo one guessed correctly. Better luck next time!")

else:
    print("\nSingleplayer mode selected!")
    play_turn("Player")
