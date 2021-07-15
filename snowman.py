SNOWMAN_WORD= 'brocolli'
encrypt_list= []


def get_letter_from_user():
    letter_from_user = input('Enter a letter: ')
    if not letter_from_user.isalpha() or len(letter_from_user) > 1:
        print("Invalid letter please enter a single character.")
        return letter_from_user
    else:
        return letter_from_user

def snowman():
    letter =  get_letter_from_user()
    if letter in SNOWMAN_WORD:
        print("letter found")
        return True
    else:
        print('Letter not found')
        return False

print(snowman())