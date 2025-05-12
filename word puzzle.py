"""
Class: CSE110 Section: A7 Student Name: Alejandro Garcia Trujillo
Project Word Puzzle
Creativity Credit Explanation: 
"""

print("Welcome to the Word Guessing Game!")

secret_word = "mosiah"
guesses = 1
# Create and show initial hint
hint = "_ " * len(secret_word)
print("Your hint is: " + hint)

# Ask for the first guess
guess = input("What is your guess? ").strip().lower()

while guess != secret_word:
    # Check if the guess length is valid
    if len(guess) != len(secret_word):
        print(f"Incorrect. Your guess must be {len(secret_word)} letters long.")
        print("Your hint is: " + "_ " * len(secret_word))
        guess = input("What is your guess? ").strip().lower()
        guesses += 1
        continue

    # Create a list to build the hint ["_", "_", "_", ...]
    hint = [None] * len(secret_word)

    # Count the letters in the secret word
    letter_count = {}
    for char in secret_word:
        letter_count[char] = letter_count.get(char, 0) + 1

    # FIRST PASS: Check for correct letters in the correct spot (uppercase)
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint[i] = guess[i].upper()  # Uppercase for correct position
            letter_count[guess[i]] -= 1  # Use up one of this letter

    # SECOND PASS: Check for correct letters in the wrong spot (lowercase)
    for i in range(len(secret_word)):
        if hint[i] is None:  # Only handle if not already matched
            if guess[i] in letter_count and letter_count[guess[i]] > 0:
                hint[i] = guess[i].lower()  # Lowercase for wrong position
                letter_count[guess[i]] -= 1
            else:
                hint[i] = "_"  # Not in the word at all

    # Show the hint with spaces between each character
    print("Incorrect. Try again.")
    print("Your hint is: " + " ".join(hint))

    # Ask for a new guess
    guess = input("What is your guess? ").strip().lower()
    guesses += 1

# If guess is correct, exit loop and show result
print(f"Correct! It took you {guesses} guesses.")