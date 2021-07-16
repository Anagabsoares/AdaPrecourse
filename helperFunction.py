import random

RANGE_LOW = 0
RANGE_HIGH = 100
# pick a random number
random_number = random.randint(RANGE_LOW, RANGE_HIGH)


def input_user_string():
    user_input_string= input('Guess the number: ')
    user_input = None
    if user_input_string.isnumeric():
        user_input = int(user_input_string)
    else:
        print("You must input a number!")    
    return user_input


def guess_the_number():
    user_input = input_user_string()
    if user_input < RANGE_LOW or user_input > RANGE_HIGH:
        print(f"Your guess is out of bounds.")
        print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
    elif user_input == random_number:
        print("You guessed the number!  Good job!")
    elif user_input > random_number:
        print("Your guess is too high")
    elif user_input < random_number:
        print("Your guess is too low")

guess_the_number()        