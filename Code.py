logo = """
 _____                                         _  _    _            _____                                   
|  __ \                                       (_)| |  | |          |_   _|                                  
| |  \/ _   _   ___  ___  ___       __      __ _ | |_ | |__          | |    __ _  _   _  _   _   __ _  _ __ 
| | __ | | | | / _ \/ __|/ __|      \ \ /\ / /| || __|| '_ \         | |   / _` || | | || | | | / _` || '__|
| |_\ \| |_| ||  __/\__ \\__ \       \ V  V / | || |_ | | | |         | |  | (_| || |_| || |_| || (_| || |   
 \____/ \__,_| \___||___/|___/        \_/\_/  |_| \__||_| |_|        \_/   \__,_| \__, | \__, | \__,_||_|   
                                                                                   __/ |  __/ |             
                                                                                  |___/  |___/     

"""
import random
print(logo)
print("Welcome to my Guessing Game!")
print("I'm thinking of a number, do you want to guess it?")

difficulty = input("Please choose a difficulty. Type easy or hard: ")

if difficulty == "easy":
    guess = int(input("Now, make your guess: "))
    number = random.randint(1,10)
    attempts = 5
    while guess != number:
        if guess < number:
            attempts -= 1
            print("Too low! Remaining attempts: " + str(attempts))
        elif guess > number:
            attempts -= 1
            print("Too high! Remaining attempts: " + str(attempts))

        guess = int(input("Make your guess:"))

    print("You guessed it!")

elif difficulty == "hard":
    guess = int(input("Now, make your guess: "))
    number = random.randint(1,100)
    attempts = 10
    while guess != number:
        if guess < number:
            attempts -=1
            print("Too low! Remaining attempts: " + str(attempts))
        else:
            attempts -=1
            print("Too high! Remaining attempts: " + str(attempts))

        guess = int(input("Make your guess:"))

    print("Winner winner chicken dinner!")

else:
    print("Invalid input, please try again!")
    