from pprint import pprint

def addiere_kw(**kwargs):
    sum = 0
    pprint(kwargs)
    for a in kwargs.values():
        sum += a
    return sum

def addiere_a(*args):
    sum = 0
    pprint(args)
    for a in args:
        sum += a
    return sum

    
    
summe = addiere_kw(a=1, b=2, c=7, f=5)
print(summe)

summe = addiere_a(1, 2, 7, 5)
print(summe)
