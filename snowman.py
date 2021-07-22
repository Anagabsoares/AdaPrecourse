import random
from wonderwords import RandomWord

SNOWMAN_WRONG_GUESSES  = 7
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_GRAPHIC = ['*   *   *  ',
            ' *   _ *   ',
            '   _[_]_ * ',
            '  * (")    ',
            '  \( : )/ *',
            '* (_ : _)  ',
            '-----------']





def get_letter_from_user( wrong_guessed_list, snowman_dict):
    flag_one_letter = False
    letter_from_user = None
    while not flag_one_letter:
        letter_from_user = input('Enter a letter: ')
        if not letter_from_user.isalpha():
            print("Invalid character, please enter a letter.")
        elif len(letter_from_user) > 1:
            print('You should input one single letter.')
        elif letter_from_user in wrong_guessed_list:
            print('You have already guessed that letter')
        elif letter_from_user in snowman_dict and snowman_dict[letter_from_user] == True :
            print(f'You have already guesses that letter {letter_from_user} and it is in the word')
        else:
            flag_one_letter = True
    return letter_from_user


def snowman():

    r = RandomWord()
    snowman_word = r.word(
    word_min_length = SNOWMAN_MIN_WORD_LENGTH, word_max_length = SNOWMAN_MAX_WORD_LENGTH)
    print(snowman_word)
    flag_correct_guess= False
    count_correct_guesses = 0
    count_wrong_guesses = 0
    wrong_guessed_list = []
    snowman_dict = snowman_word_dict(snowman_word)
    while not flag_correct_guess and count_wrong_guesses < SNOWMAN_WRONG_GUESSES: 
        letter =  get_letter_from_user(wrong_guessed_list, snowman_dict)
        print(letter)
        if  letter in snowman_dict:
            print(f"you guessed one letter that is in our word!")
            snowman_dict[letter] = True
            # correct_guessed_list.append(letter)
            # count_correct_guesses += 1
            # if count_correct_guesses == SNOWMAN_WRONG_GUESSES:     
        else:
            print(f"The letter {letter} is not in the word ")
            wrong_guessed_list.append(letter)
            count_wrong_guesses += 1

        print(snowman_dict)
        draw_snowman(count_wrong_guesses)
        print(wrong_guessed_list)    
    result = f"You made {count_correct_guesses} correct and {count_wrong_guesses} incorrect guesses" 
    return result
            
def draw_snowman(wrong_guesses_count):
    for i in range(SNOWMAN_WRONG_GUESSES - wrong_guesses_count,
                SNOWMAN_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])


def snowman_word_dict(word):
    word_dict= {}
    for letter in word:
        if not letter in word_dict:
            word_dict[letter] = False
    print(word_dict)
    return word_dict


snowman()    
  
