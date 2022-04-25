

def mean(*args): # function with unknown number of args
    return sum(args) / len(args)


print(mean(1, 2, 3, 4, 5, 100))

# keyword args
def meankw(**kwargs):
    return sum(kwargs.values()) / len(kwargs)

print(meankw(a=1, b=2, c=3, d=4, e=5, f=100))