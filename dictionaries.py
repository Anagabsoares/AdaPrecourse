dictionary = {"dog":"cat", "tree":"bush", "star":"planet"}

def get_value_from_dictionary(dictionary, key):
    result = ""
    if key in dictionary:
        result = dictionary[key]
        print(result)
    else:
        result = None
        print(result)
    return result


get_value_from_dictionary(dictionary, "dog")