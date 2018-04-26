def my_range(low, high):
    current = low
    while current <= high:
        yield current
        current += 1

def my_range_a(low, high):
    current = low
    return range(low, high+1)
        
        
for i in my_range_a(1,10):
    print(i)
    
    
a = [1,2,3,4]

def my_list_iter(field):
    for e in field:
        yield e
        
for c in my_list_iter(a):
    print(c)

print(a)    