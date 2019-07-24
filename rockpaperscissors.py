import random

playerScore = 0
aiScore = 0

while True:
    choice = input("Choose rock, paper or scissors\n").lower()

    if choice == "rock" or choice == "paper" or choice == "scissors":
        temp = random.randint(1, 3)
        if temp == 1:
            aiChoice = "rock"
        elif temp == 2:
            aiChoice = "paper"
        elif temp == 3:
            aiChoice = "scissors"

        if choice == aiChoice:
            print("I choose {}. The game was a tie!".format(aiChoice))
        elif choice == "rock":
            if aiChoice == "paper":
                print("I choose {}. I win!".format(aiChoice))
                aiScore += 1
            elif aiChoice == "scissors":
                print("I choose {}. You win!".format(aiChoice))
                playerScore += 1
        elif choice == "paper":
            if aiChoice == "scissors":
                print("I choose {}. I win!".format(aiChoice))
                aiScore += 1
            elif aiChoice == "rock":
                print("I choose {}. You win!".format(aiChoice))
                playerScore += 1
        elif choice == "scissors":
            if aiChoice == "rock":
                print("I choose {}. I win!".format(aiChoice))
                aiScore += 1
            elif aiChoice == "paper":
                print("I choose {}. You win!".format(aiChoice))
                playerScore += 1

        print("You: {} - AI: {}".format(playerScore, aiScore))

        if input("Play again? (Y/N)\n").lower() != "y":
            break
    else:
        print("Rock, paper or scissors are your only options")
