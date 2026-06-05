#Hangman game- CodeAlpha Internship

import random

words = ["apple", "book", "cat", "python", "code"]
word = random.choice(words)

guessed = []
tries = 6

while tries > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("Word:", display)

    if "_" not in display:
        print("You won!")
        break

    guess = input("Guess a letter: ")

    if guess in word:
        guessed.append(guess)
    else:
        tries -= 1
        print("Wrong! Tries left:", tries)

if tries == 0:
    print("You lost! Word was:", word)