SNOWMAN_WORD= 'snowman'
SNOWMAN_WRONG_GUESSES  = 7
SNOWMAN_1 = '*   *   *  '
SNOWMAN_2 = ' *   _ *   '
SNOWMAN_3 = '   _[_]_ * '
SNOWMAN_4 = '  * (")    '
SNOWMAN_5 = '  \( : )/ *'
SNOWMAN_6 = '* (_ : _)  '
SNOWMAN_7 = '-----------'
encrypt_list= []


def get_letter_from_user():
    flag_one_letter = False
    letter_from_user = None
    while not flag_one_letter:
        letter_from_user = input('Enter a letter: ').lower()
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
        if  letter in SNOWMAN_WORD:
            count_correct_guesses += 1
            if count_correct_guesses == SNOWMAN_WRONG_GUESSES:
                flag_correct_guess = True     
        else:
            count_wrong_guesses += 1
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