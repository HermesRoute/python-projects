import random

def computer_guess(x):
    minimum = 1
    maximum = x
    feedback = ""

    while feedback != "c":
        if minimum != maximum:
            guess = random.randint(minimum, maximum)
        else:
            guess = minimum

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C): ")

        if feedback.lower() == "h":
            maximum = guess - 1
        elif feedback.lower() == "l":
            minimum = guess + 1

    print(f"You gave the number {x} and the computer guessed {guess} correctly!")

computer_guess(10)