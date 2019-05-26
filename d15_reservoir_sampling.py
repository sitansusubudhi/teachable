import random

def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        value = random.randint(1, i + 1) 
        if value == 1:
            print(value," idx ",i)
            random_element = e
    return random_element

print("Random ",pick([1,2,3,4,5]))