import random

# List of predefined words
words = ["python", "apple", "tiger", "ocean", "chair"]

# Randomly choose a word
word = random.choice(words)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

# Display welcome message
print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

# Main game loop
while incorrect_guesses < max_incorrect:

    # Display the word with blanks
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player won
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single alphabet letter.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    # Add guess to guessed letters
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("✅ Correct guess!")
    else:
        incorrect_guesses += 1
        remaining = max_incorrect - incorrect_guesses
        print("❌ Wrong guess!")
        print("Remaining attempts:", remaining)

# If player loses
if incorrect_guesses == max_incorrect:
    print("\n💀 Game Over!")
    print("The correct word was:", word)