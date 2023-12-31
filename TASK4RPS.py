import random

# Initialization of scoring
Your_score = 0
computer_score = 0

# Define the choices for the uses
choices = ["rock", "paper", "scissors"]

print("Prashant's Game Hub")

def get_user_choice():
    while True:
        Your_choice = input("Choose rock, paper, or scissors: ").lower()
        if Your_choice in choices:
            return Your_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    global Your_score
    global computer_score

    print("Rock, Paper, Scissors Game")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"User Score: {Your_score}")
        print(f"Computer Score: {computer_score}")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
