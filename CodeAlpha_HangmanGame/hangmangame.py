import random

word_list = ["apple", "banana", "mango", "orange", "grapes"]
secret_word = random.choice(word_list)
guessed_word = ["_"] * len(secret_word)

max_attempts = 6
wrong_guesses = 0
guessed_letters = []

print("Welcome to Hangman Game")

while wrong_guesses < max_attempts and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    print("Remaining attempts:", max_attempts - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input")
        continue

    if guess in guessed_letters:
        print("Already guessed")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
    else:
        wrong_guesses += 1

if "_" not in guessed_word:
    print("\nYou won! The word was:", secret_word)
else:
    print("\nGame Over! The word was:", secret_word)