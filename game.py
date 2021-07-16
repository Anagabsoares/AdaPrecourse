import random

RANGE_LOW = 0
RANGE_HIGH = 100

random_numer = random.randint(RANGE_LOW, RANGE_HIGH)




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


get_number_from_user()                