numberOfFrames = 2
numberOfBallsOfFrames = 2
maxNumRolls = (numberOfFrames * numberOfBallsOfFrames)
score = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0,0]]
 
 
def getUserInput():
    roll = int(input("How many pins did you knock down? 0-10"))
    return roll
 
def checkforStrike(ball,score):
    if (ball == 0 and score == 10):
        return ("Strike!")
  
 
def game():
    frame = 0
    frameRoll = 1
    for frame in range(numberOfFrames):
        for frameRoll in range(numberOfBallsOfFrames):
            playerScore = getUserInput()
            checkStrike = checkforStrike(frameRoll,playerScore)
            if checkStrike == "Strike!":
                print("Strike!")
                print(numberOfBallsOfFrames)
                print(frame,frameRoll)
                score[frame][frameRoll - 1] = playerScore
                frameRoll = frameRoll+1
            else:
                score[frame][frameRoll - 1] = playerScore
                print(frame,frameRoll)
        frameRoll = 0
 
game()
print(score)
 