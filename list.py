

def find_index_of_item(item, list_of_items):
    if item in list_of_items or list_of_items.count(item) > 1:
        return list_of_items.index(item)
    else:
        return -1

a = ["a", "c", "b", "c"]        


def total(item, a):
    print(a.count(item))



flavors = ["vanilla", "chocolate", "strawberry"]
toppings = ["whipped cream", "nuts", "a cherry"]
def icecreams_sundae(flavors, toppings):
    result= []
    for i in flavors:
        for j in toppings:
            result.append(f"{i} with {j}")
    return(result)
icecreams_sundae(flavors, toppings)    