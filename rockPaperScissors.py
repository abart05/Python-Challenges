import random

def play_game():
    rounds = 0 
    playerScore = 0
    computerScore = 0
    
    valid_choices = ["rock", "paper", "scissors"]

    while rounds < 3:

        player_choice = input("Please choose either Rock, Paper, or Scissors: ").lower()
        if player_choice not in valid_choices:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            player_choice = input("Please choose either Rock, Paper, or Scissors: ").lower()
        
        
        computer_choice = random.choice(valid_choices)
        
        print(f"\nPlayer chooses: {player_choice.capitalize()}")
        print(f"Computer chooses: {computer_choice.capitalize()}\n")
        
        if player_choice == computer_choice:
            playerScore += 1
            computerScore += 1
            print("It's a draw!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
            playerScore += 1
            print("Player wins!")
        else:
            computerScore += 1
            print("Computer wins!")
        rounds += 1
        print(f"Score is: Player {playerScore} - Computer {computerScore}")

        
play_game()
