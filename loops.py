# #
# def print_ten(word):
#     counter= 0
#     final_value = '' 
#     for item in range(0,10):
#         if counter > 1:
#             final_value += " "
#         counter = counter + 1 
#         value = str(counter)
#         final_value += value + ' '
#         final_value += " "
#         final_value += word
#     return final_value


# word = "hallo"

# print(print_ten(word))

# def print_multiple(word= str(), amount=int()):
#     counter= 0
#     final_value = '' 
#     for item in range(1,amount+1):
#         value = str(counter)
#         final_value += value
#         final_value = " "
#         final_value =
#         counter = counter + 1 

#     print(value.strip()) 

#     return final_value

# def print_ten(word):
#     value = ''
    
#     for item in range(0,10):
#         value += f'{str(item+1)} {word} ' 
#     if word == '':
#         return value[:-1]
#     else:
#         return value.strip() 

# def print_ten(word):
#     value = ''
#     for item in range(0,10):
#         value += f'{str(item+1)} {word} ' 
#     if word == '':
#         return value[:-1]
#     else:
#         return value.strip() 

# def print_ten(word):
#     count = 1
#     result = ""
#     while count < 11:
#         if count > 1:
#             result += " "
#         result += str(count)
#         result += " "
#         result += word
#         count += 1

#     return result

def print_ten(word):
    value = ''
    for item in range(1,11):
        if item > 1:
            value += " " #add space after word 
        value += f'{item} {word}'
    return value


def print_multiple(word, amount):
    final_value = '' 
    for item in range(1, amount+1):
        if item > 1:
            final_value += " "
        final_value += f'{item} {word}'
    return final_value


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