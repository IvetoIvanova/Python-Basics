# Unscramble it!

"Unscramble it!" is a simple word puzzle game where players must guess the correct word from a scrambled set of letters.
Now with difficulty levels, multiplayer mode, and word loading from an external file!


## 📝 How to play

1. The program selects a random word from a **word list** (`words.txt`).
2. The letters of the word are scrambled and displayed.
3. Players must **unscramble** the word within a limited number of attempts.
4. **Singleplayer mode**: The player has 3 attempts to guess the correct word.
5. **Multiplayer mode**: Two players take turns to guess words. The player with the most correct guesses wins!
6. If the player **guesses correctly**, they score a point! 🎉
7. If they fail, the correct word is revealed.

## 📌 Features

✅ Random word selection from `words.txt`  
✅ Three difficulty levels (Easy, Medium, Hard)  
✅ Singleplayer & multiplayer mode  
✅ Scrambles the word using `random.shuffle()`  
✅ Allows up to 3 attempts  
✅ Ignores uppercase/lowercase differences  
✅ Displays the remaining attempts  
✅ Game continues for multiple rounds until players choose to end it

## 🖥️ Installation & Running the Game

1. **Make sure you have Python 3 installed**
2. **Download the script or clone the repository.**
3. **Ensure `words.txt` is in the same directory as the script.**
4. **Run the script:**
   ```sh
   python unscramble_it.py

## ⚙️ Game modes
**🎮 Singleplayer mode**

The player must unscramble words within 3 attempts per word.

The game continues until they choose to end or run out of words.

**👥 Multiplayer mode**

Two players take turns guessing words.

The game keeps track of scores based on correct answers.

The player with the highest score at the end wins.

## 🚀 Future Improvements

* ✅ (Done) Load words from an external file instead of a predefined list

* ✅ (Done) Add difficulty levels (easy, medium, hard)

* ✅ (Done) Implement a multiplayer mode

## 📜 License

This game is open-source and free to use. Feel free to contribute or modify it as needed!
