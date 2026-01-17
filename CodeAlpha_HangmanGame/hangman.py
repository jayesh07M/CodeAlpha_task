import random

word_list = ["apple", "banana", "mango", "strawberry", "orange", "pomegranate"]
secret_word = random.choice(word_list)
guessed_word = ["_"] * len(secret_word)
wrong_guess = 0
max_attempt = 6
guessed_letters = []

print("Welcome to Jayesh's Hangman! Find the fruit!")

while wrong_guess < max_attempt and "_" in guessed_word:
    print("\nCurrent word: " + " ".join(guessed_word))
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Great guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        wrong_guess += 1
        print(f"Chances left: {max_attempt - wrong_guess}")

if "_" not in guessed_word:
    print("\nYour guess is correct. Congrats! The word was:", secret_word)
else:

    print("\nGame over. The word was:", secret_word)