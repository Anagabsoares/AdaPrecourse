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


dict = {"dog":1, "tree":1, "star":4}

def dict_counter(dict, key):
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1
    print(dict)
    return dict

dict_counter(dict,"tree")


keys=[1, 2,]
values=["dog", "cat", "bird", "mouse"]

def build_a_dictionary(keys, values):
    dictionary = {}
    if not keys or  len(keys) != len(values):
        dictionary = None
    else:
        for index in range(len(keys)):
            value = values[index]
            key = keys[index]
            dictionary[key] = value
    return dictionary

build_a_dictionary(keys, values) 

# ANOTHER OPTION
# def build_a_dictionary(keys, values):
#     if not len(keys) == len(values):
#         return None
#     result = {}
#     for key, value in zip(keys, values):
#         result[key] = value
#     return result