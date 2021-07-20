SNOWMAN_WORD= 'snow'
SNOWMAN_WRONG_GUESSES  = 7
encrypt_list= []


def get_letter_from_user():
    flag_one_letter = False
    letter_from_user = None
    while not flag_one_letter:
        letter_from_user = input('Enter a letter: ')
        if not letter_from_user.isalpha():
            print("Invalid character, please enter a letter.")
        elif len(letter_from_user) > 1:
            print('You should input one single letter.')
        else:
            flag_one_letter = True
    return letter_from_user

def snowman():
    flag_correct_guess= False
    count_correct_guesses = 0
    count_wrong_guesses = 0
    while not flag_correct_guess and count_wrong_guesses < SNOWMAN_WRONG_GUESSES: 
        letter =  get_letter_from_user()
        if count_correct_guesses == SNOWMAN_WRONG_GUESSES:
            flag_correct_guess == True
        elif letter in SNOWMAN_WORD:
            count_correct_guesses += 1
            print("letter found") 
        else:
            count_wrong_guesses += 1
            print('Letter not found')
    print(f"You made {count_correct_guesses} correct and {count_wrong_guesses} incorrect guesses")
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





