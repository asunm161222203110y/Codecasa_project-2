import random
def play_rps(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"Your choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"

# Get user input
user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

# Check if the input is valid
if user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice. Please choose rock, paper, or scissors.")
else:
    result = play_rps(user_choice)
    print(result)
