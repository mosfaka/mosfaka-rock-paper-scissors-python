import random

# Function to get player and computer choices
def get_choices():
    player_choice = input("Enter a choice (rock, paper or scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choices = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choices}

    return choices

# Function to check who wins
def check_win(player, computer):
    print(f"You chose {player} \nComputer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "You win!"
        else:
            return "You lose."
    elif player == "paper":
        if computer == "rock":
            return "You win!"
        else:
            return "You lose."
    elif player == "scissors":
        if computer == "paper":
            return "You win!"
        else:
            return "You lose."
    else:
        return "Invalid choice. Please choose (rock, paper or scissors)"

# Run the game
game_choices = get_choices()
result = check_win(game_choices["player"], game_choices["computer"])
print (result)        