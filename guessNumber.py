import random
 
def guess_number():
    rounds = 1
    playerScore = 0
    computerScore = 0
    for rounds in range (3):
        user = int(input("Can you guess the number I'm thinking of... Please enter 1, 2 or 3: "))
        number = [1, 2, 3]
        randomNumber = random.choice(number)
        if user >3 or user <1:
            user = input("Please enter 1, 2 or 3: ")
           
        elif user == randomNumber:
            print(f"Congrats, you guess the number im thinking of {randomNumber}.")
            playerScore += 1
        else:
            print(f"Incorrect. I was thinking of the number {randomNumber}.")
            computerScore += 1
        print(f"The current score is: Player {playerScore} - Computer {computerScore}")
    rounds += 1
    if playerScore > computerScore:
        print(f"Congratulations, you beat me by {playerScore} - {computerScore}.")
    else:
        print(f"Unlucky, I beat you {computerScore} - {playerScore}.")
 
guess_number()