#Function - a named chunck of code that is callable and performs a task.
# Functions can contain parameters - values to be passed into functions
# Start Function Signature
import random



def function_name(some_parameter, another_parameter): # End of Function Signature
    # Start of Function Body
    print(some_parameter, another_parameter)
    # End of Function Body

function_name('a','b')    

value = random.randint(1,100)
print(value)

def guess_the_number( value ):
    number_guessed = input('What is the number guessed?')
    if number_guessed.isnumeric():
        user_input_integer = int(number_guessed)
        print(number_guessed)
        if user_input_integer == value:
            print(f'You won, the misterious value is {value}')  
            return  
        if user_input_integer > value:
            print("The number entered is to high")
            return
        else:
            print('The number entered is to low ')
            return    
    else: 
        while not number_guessed.isnumeric():
            print("Enter a numberrrr")
            user_input= input("Guessss the number: ") 
            if user_input.isnumeric():
                return guess_the_number(user_input)
                    

guess_the_number(value)
