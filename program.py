import random
while True:
    print("welcome user")
    print("Let's play a guessing game!")
    print("chose your difficulty level:")
    print("easy: 10 guesses")
    print("medium: 7 guesses")
    print("hard: 5 guesses")
    difficulty = input("Please enter 'easy', 'medium', or 'hard': ")
    secret_number = random.randrange(1, 101)

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "medium":
        attempts = 7
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Invalid difficulty level.")
        exit()

    for i in range(attempts):
        print("Attempt", i + 1)
        guess = int(input("Please enter your guess (between 1 and 100): "))
        if guess == secret_number:
            print("Congratulations! You've guessed the number!")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
    print("do you want to play again? (yes/no)")
    play_again = input().lower()
    if play_again != "yes":
        break
