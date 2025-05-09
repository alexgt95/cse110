"""
Class: CSE110 Section: A7 Student Name: Alejandro Garcia Trujillo
Project Word Puzzle
Creativity Credit Explanation: 
"""

print("Welcome to the Word Guessing Game!")

secret_word = "mosiah"
hint = "_ " * len(secret_word) # Same as [ _ _ _ _ _ _ ] [ M o s i a h ]
print("Your hint is: " + hint)
guess = input("What is your guess? ").strip().lower()
guesses = 1

while guess != secret_word:
    if len(guess) != len(secret_word):
        print("Incorrect. Your guess must be " + str(len(secret_word)) + " letters long.")
        guess = input("What is your guess? ").strip().lower()
        print("Your hint is: " + hint)
        guesses += 1
        continue
    # If the guess is the same length as the secret word, check for correct letters
    #Check if the letter is in the word and if it is in the correct position
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            hint.append(guess[i].upper())  # Correct letter and spot
            guess[i] -= 1  # Decrement the count of this letter
        else:
            hint.append(None)  # Placeholder for now
    hint = " ".join(hint)
    # Fill in the hint with underscores for incorrect letters
    for i in range(len(secret_word)):
        if hint[i] is None:
            hint[i] = "_ "
        else:
            hint[i] = hint[i].lower() + " "
    hint = " ".join(hint)
    #Check if the letter is in the word but not in the correct position
    for i in range(len(secret_word)):
        if guess[i] != secret_word[i] and guess[i] in secret_word:
            hint[i] = guess[i].lower() + " "  # Correct letter but wrong spot
        else:
            hint[i] = "_ "
    hint = " ".join(hint)

    print("Incorrect. Try again.")
    print("Your hint is: " + hint)
    guess = input("What is your guess? ").strip().lower()
    guesses += 1



if guess == secret_word:
    print("Correct! It took you " + str(guesses) + " guesses.")