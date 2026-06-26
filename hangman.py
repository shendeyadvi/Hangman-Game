import random

# list of predefined words 
words = ["apple", "python", "computer", "school", "data"]

# select random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
attempts = 6

print("------- HANGMAN GAME -------")

while incorrect_guesses < attempts:
    display_word =""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You've guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Wrong Guess")
        print("Remaining attempts:", attempts - incorrect_guesses)

if incorrect_guesses == attempts:
    print("Game Over!")
    print("The correct word was:", word)