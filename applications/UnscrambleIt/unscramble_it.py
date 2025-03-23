import random

words = ["python", "developer", "console", "programming", "challenge"]
word = random.choice(words)
scrambled = list(word)
random.shuffle(scrambled)
scrambled = "".join(scrambled)

print("Welcome to 'Unscramble it!'")
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
