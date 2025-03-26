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

print("Welcome to 'Unscramble it!'")
print("Choose a difficulty level:")
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

word = random.choice(selected_words)
scrambled = list(word)
random.shuffle(scrambled)
scrambled = "".join(scrambled)

print("You have 3 attempts to guess the correct word.")
print(f"Scrambled word: {scrambled}")

attempts = 3

for i in range(attempts):
    guess = input(f"Attempt {i + 1}/{attempts} - Unscramble the word: ").strip().lower()

    if guess == word.lower():
        print("Congratulations! You guessed the word.")
        break
    else:
        remaining_attempts = attempts - (i + 1)
        if remaining_attempts > 0:
            print(f"Wrong answer! Try again. You have {remaining_attempts} attempts left.")
        else:
            print(f"Game over! The correct word was '{word}'.")
