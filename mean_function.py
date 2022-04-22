

def mean(value):  # mean function
    if isinstance(value, dict): # if value is a dictionary
        the_mean = sum(value.values())/len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean


listz = [1, 2, 3, 4, 5]

dictz = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(mean(listz))

print(mean(dictz))
3