# Conditionals - if, else, elif
import random
# random.randit will generate a randon INTEGER ion a range

print(random.randint(1,10))

car = "1"

#
print(car.isnumeric())
# check if a STRING is numericy
# true
user_input = input("Guess the number: ") 




if user_input.isnumeric():
        user_input_integer = int(user_input)
        print('number')   
else:        
    while not user_input.isnumeric():         
        print('You should enter a number!')  
        user_input = input("Guess the number: ") 
        if user_input.isnumeric():
            user_input_integer = int(user_input)
            print('you finally entered a number!')       

pocket_change = 112

if pocket_change < 100:
    print("You have less than a dollar in change.")
if pocket_change > 100:
    print("You have more than a dollar in change.")
if pocket_change > 100 and pocket_change < 500:
    print("You have at least four dollars in change.")
if pocket_change > 500:
    print("That's a lot of change!!!")
# if each statement is checked


if pocket_change < 100:
    print("You have less than  in change.")
elif pocket_change > 100:
    print("You have more than a dollar in change.")
elif pocket_change > 100 and pocket_change < 500:
    print("You have at least four dollars in change.")
else:
    print("That's a lot of change!!!")
