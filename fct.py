b = 2

def add(a, b, c):
    sum = a + b + c    
    b += 1
    print('aus fkt', b)
    return sum


print(add(1, b, 3))
print(b)

