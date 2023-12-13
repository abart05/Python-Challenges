score = []

def getPlayersScore():
    while True:
        #frame1
        roll1 = int(input("Frame 1: How many pins did you knock down? 0-10"))
        if roll1 == 10:
         print("Strike!")
         score.append(roll1)
        else:
            roll2 = int(input("How many pins did you knock down? 0-remaining pins"))
            if roll1 + roll2 == 10:
                print("Spare!")
            score.append(roll1 + roll2)
        #frame2
        roll1 = int(input("Frame 2: How many pins did you knock down? 0-10"))
        if roll1 == 10:
         print("Strike!")
         score.append(roll1)
        else:
            roll2 = int(input("How many pins did you knock down? 0-remaining pins"))
            if roll1 + roll2 == 10:
                print("Spare!")
            score.append(roll1 + roll2)
           
        #frame3
        roll1 = int(input("Frame 3:How many pins did you knock down? 0-10"))
        if roll1 == 10:
         print("Well done, you scored a strike!")
         score.append(roll1)
        else:
            roll2 = int(input("How many pins did you knock down? 0-remaining pins"))
            if roll1 + roll2 == 10:
                print("Spare!")
            score.append(roll1 + roll2)
           
        #frame4
        roll1 = int(input("Frame 4: How many pins did you knock down? 0-10"))
        if roll1 == 10:
         print("Well done, you scored a strike!")
         score.append(roll1)
        else:
            roll2 = int(input("How many pins did you knock down? 0-remaining pins"))
            if roll1 + roll2 == 10:
                print("Spare!")
            score.append(roll1 + roll2)
           
        #frame5
        roll1 = int(input("Frame 5: How many pins did you knock down? 0-10"))
        if roll1 == 10:
         print("Well done, you scored a strike!")
         score.append(roll1)
        else:
            roll2 = int(input("How many pins did you knock down? 0-remaining pins"))
            if roll1 + roll2 == 10:
                print("Spare!")
            score.append(roll1 + roll2)
           
        #frame6
        roll1 = int(input("Frame 6: How many pins did you knock down? 0-10"))
        if roll1 == 10:
         print("Well done, you scored a strike!")
         score.append(roll1)
        else:
            roll2 = int(input("How many pins did you knock down? 0-remaining pins"))
            if roll1 + roll2 == 10:
                print("Spare!")
            score.append(roll1 + roll2)
           
        #frame7
        roll1 = int(input("Frame 7: How many pins did you knock down? 0-10"))
        if roll1 == 10:
         print("Well done, you scored a strike!")
         score.append(roll1)
        else:
            roll2 = int(input("How many pins did you knock down? 0-remaining pins"))
            if roll1 + roll2 == 10:
                print("Spare!")
            score.append(roll1 + roll2)
           
        #frame8
        roll1 = int(input("Frame 8: How many pins did you knock down? 0-10"))
        if roll1 == 10:
         print("Well done, you scored a strike!")
         score.append(roll1)
        else:
            roll2 = int(input("How many pins did you knock down? 0-remaining pins"))
            if roll1 + roll2 == 10:
                print("Spare!")
            score.append(roll1 + roll2)
           
        #frame9
        roll1 = int(input("Frame 9: How many pins did you knock down? 0-10"))
        if roll1 == 10:
         print("Well done, you scored a strike!")
         score.append(roll1)
        else:
            roll2 = int(input("How many pins did you knock down? 0-remaining pins"))
            if roll1 + roll2 == 10:
                print("Spare!")
            score.append(roll1 + roll2)
           
        #frame10 - with bonus round
        roll1 = int(input("Frame 10: How many pins did you knock down? 0-10"))
        if roll1 == 10:
         print("Well done, you scored a strike!")
         score.append(roll1)
        else:
            roll2 = int(input("How many pins did you knock down? 0-remaining pins"))
            if roll1 + roll2 == 10:
                print("Spare!")
            score.append(roll1 + roll2)
       
        roll3 = int(input("Bonus Roll. How many pins did you knock down? 0-10"))
        score.append(roll3)
        if roll3 == 10:
         print("Well done, you scored a strike!")
       
        print("Your total score is:" , sum(score))
        break
getPlayersScore() 
 