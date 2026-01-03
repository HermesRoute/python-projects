import random
from words import words_list
import string

def hangman():
    word = random.choice(words_list).upper()
    print(word)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:

        print("You have used these letters: ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(f"Current lives remaining: {lives} ----- Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Your letter isn't in the word!")

        elif user_letter in used_letters:
            print("You have already guessed this letter. Please try again.")

        else:
            print("Invalid letter, please try again.")

    if lives == 0:
        print(f"You died. The word was {word}")
    else:
        print(f"You guessed the word {word} correctly.")

hangman()