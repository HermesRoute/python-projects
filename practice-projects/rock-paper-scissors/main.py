import random

def game():
    choices = ["r", "p", "s"]
    continue_game = True

    while continue_game:
        user_choice = input("(r)Rock, (p)Paper, (s)Scissors: ")
        computer_choice = random.choice(choices)

        game_result = result(user_choice, computer_choice)

        if game_result == "Tie":
            print(f"Tied game, you chose {user_choice} and the computer chose {computer_choice}")
            continue
        else:
            print(f"You chose {user_choice} and the computer chose {computer_choice}.")
            print(game_result)
            continue_game = False

def result(user_choice, computer_choice):
    # p > r, r > s, s > p
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "p" and computer_choice == "r") or (user_choice == "r" and computer_choice == "s") or (user_choice == "s" and computer_choice == "p"):
        return "User Win"
    else:
        return "Computer Win"

game()