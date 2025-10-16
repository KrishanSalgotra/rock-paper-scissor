import random

# Define possible choices
choices = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
while True:
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
    if user_choice == "quit":
        print("Thanks for playing!")
        break
    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)