import random

RANGE_LOW = 1
RANGE_HIGH = 100
MAX_GUESSES = 4

random_number = random.randint(RANGE_LOW, RANGE_HIGH)




def get_number_from_user():
    valid_input = False #flag variable
    user_input = None
    while not valid_input:
        user_input_string = input("Guess the number: ")
        
        if user_input_string.isnumeric():
            user_input = int(user_input_string)
            valid_input = True #change the flag variable value when conditional is met
        else:
            print("You must input a number!")
    print(user_input)       
    return user_input


def guessed_number_right():
    random_number = random.randint(RANGE_LOW, RANGE_HIGH)
    print(random_number)
    guessed_right = False
    num_guesses = 0
    while not guessed_right and num_guesses < MAX_GUESSES:
        user_input = get_number_from_user()
        num_guesses+=1
        print(num_guesses)
        if user_input < RANGE_LOW or user_input > RANGE_HIGH:
            print(f'your guess  is out of bounds.')
            print(f'It must be between {RANGE_LOW} and {RANGE_HIGH}')
        elif user_input == random_number:
            print("You guessed the number!  Good job!")
            guessed_right = True
        elif user_input > random_number:
            print("Your guess is too high")   
        elif user_input < random_number:
            print("Your guess is too low") 
    if num_guesses == MAX_GUESSES and not guessed_right:
        print('YOU EXCESSED THE GUESSES LIMIT')     
    return f' The number is {random_number}'


guessed_number_right()
