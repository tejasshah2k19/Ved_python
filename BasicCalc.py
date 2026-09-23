def add(a,b):
    return a+b

def mul(a,b):
    return a*b 


def sum(*args):
    sum = 0 
    for data in args:
        sum = sum + data
    return sum