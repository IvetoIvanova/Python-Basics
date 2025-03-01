import math

most_powerful_word = ""
max_power = 0

while True:
    word = input()
    if word == "End of words":
        break

    word_power = 0
    for char in word:
        word_power += ord(char)

    if word[0].lower() in "aeiouy":
        word_power *= len(word)
    else:
        word_power = math.floor(word_power / len(word))

    if word_power > max_power:
        max_power = word_power
        most_powerful_word = word

print(f"The most powerful word is {most_powerful_word} - {max_power}")
