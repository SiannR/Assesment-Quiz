import random

# Data validation
def single_letter(user_input):
    return isinstance(user_input, str) and len(user_input) == 1 and user_input.isalpha()

# Hangman picture
def draw_hangman(mistakes):
    hangman_parts = [
        "      |\n"
        "      |\n"
        "      |",
        " O    |\n"
        "      |\n"
        "      |",
        " O    |\n"
        " |    |\n"
        "      |",
        " O    |\n"
        "/|    |\n"
        "      |",
        " O    |\n"
        "/|\\   |\n"
        "      |",
        " O    |\n"
        "/|\\   |\n"
        "/     |",
        " O    |\n"
        "/|\\   |\n"
        "/ \\   |"
    ]
    print("  ____")
    print(" |    |")
    print(hangman_parts[min(mistakes, len(hangman_parts) - 1)])
    print("      |")
    print("______|___")


words = ["sky", "python", "island", "avengers", "gum", "pizza", "judge", "hangman", "lemon"]
attempts_allowed = 6
attempts = attempts_allowed
randword = random.choice(words)
randword_chars = list(randword)
randword_chars_guessed = ["_"] * len(randword_chars)
guessed_chars = []

print("Welcome to hangman.")


while not attempts == 0:
    print(" ".join(randword_chars_guessed))
    guess = input("Guess a letter: ").lower()

    # Data Valdation
    if not single_letter(guess):
        print("Please enter only a single letter.")
    elif guess in guessed_chars:
        print("You have already tried that letter.")

    # Game
    elif guess in randword_chars:
        print("Great you guessed correctly.")
        for ndx, ch in enumerate(randword_chars):
            if ch == guess:
                randword_chars_guessed[ndx] = guess
    else:
        attempts -= 1
        draw_hangman(attempts_allowed-attempts)
        print(f"Wrong.. {attempts} attempts left.")

    if not "_" in randword_chars_guessed:
        print(f"Well Done!! You still had {attempts} attempts left. The Word was:")
        print(randword)
        break

    guessed_chars.append(guess)

if attempts == 0:
    print("You ran out of guesses. The word was: ")
    print(randword)
