import random

while True:
    print(
        "Welcome to Higher or Lower! I will think of a random number between 1 and 100 and you must guess what it is!"
    )
    guess_count = 0
    number = random.randint(1, 100)
    print("Guess my number!")

    while True:
        guess = int(input())
        guess_count += 1

        if guess == number:
            print(
                "~CONGRATULATIONS~\nYou guessed my number correctly after {} attempts!".format(
                    guess_count
                )
            )
            break
        elif guess > number:
            print("Try guessing lower")
        elif guess < number:
            print("Try guessing higher")

    if input("Would you like to play again? (Y/N)\n").lower() != "y":
        break
