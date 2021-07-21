import random
from wonderwords import RandomWord

SNOWMAN_WRONG_GUESSES  = 8
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_1 = '*   *   *  '
SNOWMAN_2 = ' *   _ *   '
SNOWMAN_3 = '   _[_]_ * '
SNOWMAN_4 = '  * (")    '
SNOWMAN_5 = '  \( : )/ *'
SNOWMAN_6 = '* (_ : _)  '
SNOWMAN_7 = '-----------'





def get_letter_from_user( wrong_guessed_list, correct_guessed_list, snowman_word):
    flag_one_letter = False
    letter_from_user = None
    while not flag_one_letter:
        letter_from_user = input('Enter a letter: ')
        if not letter_from_user.isalpha():
            print("Invalid character, please enter a letter.")
        elif len(letter_from_user) > 1:
            print('You should input one single letter.')
        elif letter_from_user in wrong_guessed_list or letter_from_user in correct_guessed_list:
            print('You have already guessed that letter')
        else:
            flag_one_letter = True
    return letter_from_user


def snowman():

    r = RandomWord()
    snowman_word = r.word(
    word_min_length = SNOWMAN_MIN_WORD_LENGTH, word_max_length = SNOWMAN_MAX_WORD_LENGTH)
    flag_correct_guess= False
    count_correct_guesses = 0
    count_wrong_guesses = 0
    wrong_guessed_list = []
    correct_guessed_list = []

    print(snowman_word)
    while not flag_correct_guess and count_wrong_guesses < SNOWMAN_WRONG_GUESSES: 
        letter =  get_letter_from_user(wrong_guessed_list,correct_guessed_list, snowman_word)
        if  letter in snowman_word:
            print(f"you guessed one letter that is in our word!")
            correct_guessed_list.append(letter)
            count_correct_guesses += 1
            if count_correct_guesses == SNOWMAN_WRONG_GUESSES:
                flag_correct_guess = True     
        else:
            print(f"The letter {letter} is not in the word ")
            wrong_guessed_list.append(letter)
            count_wrong_guesses += 1

        print(correct_guessed_list)
        draw_snowman(count_wrong_guesses)
            
    result = f"You made {count_correct_guesses} correct and {count_wrong_guesses} incorrect guesses" 
    return result
            
def draw_snowman(count_wrong_guesses):
    for item in range(SNOWMAN_WRONG_GUESSES +1 - count_wrong_guesses, SNOWMAN_WRONG_GUESSES+1):
        if item  == 1:
            print(SNOWMAN_1)
        elif item == 2:
            print(SNOWMAN_2)
        elif item ==3:
            print(SNOWMAN_3)
        elif item ==4:
            print(SNOWMAN_4)   
        elif item ==5:
            print(SNOWMAN_5)
        elif item ==6:
            print(SNOWMAN_6) 
        elif item ==7:    
            print(SNOWMAN_7)  

snowman()    


# EXERCISE
# Best Burger needs help creating order_summary 
# for their drive-thru display. 
# Best Burger menu include: $5.25 burger, $2.50 fries, and a $4.25 milkshake. 
# Create the helper function calculate_total that 
# takes in a list of items and calculates the total to be used in order_summary.

# # example input items	example output (return value)
# # ['fries', 'fries', 'burger']	10.25
# # ['fries', 'milkshake', 'burger']	12


# order_items= ['fries', 'fries', 'burger']

# def calculate_total(order_items):
#     total = 0
#     for item in order_items:
#         if item == 'fries':
#             total = total + 2.50
#         if item == 'burger':
#             total += 5.25
#         if item == "milkshake":
#             total += 4.25
#     return total 
        
# def order_summary(order_items):
#     total = calculate_total(order_items)
    
#     print("*** Welcome to Best Burger ***")
#     print("Order Items: ")
#     for item in order_items:
#         print(item)
#     print(f"Total: {total}")

# order_summary(order_items)   

# # EXERCISE
# # FastBooks needs help developing an income statement generator. 
# # Given a list of expense costs, create the function calculate_expenses.
# #  This function will be used in calculate_net_income.

# # example input expense costs	example output (return value)
# # [10, 20, 30]	60


# expense_costs = [10, 20, 30]
# revenue = 1000
# def calculate_expenses(expense_costs):
#     total = 0
#     for expense in expense_costs:
#         total += expense
#     return total 
    
# def calculate_net_income(revenue, expense_costs):
#     expenses = calculate_expenses(expense_costs)
#     net_income = revenue - expenses
#     return net_income

# print(calculate_net_income(revenue, expense_costs))





