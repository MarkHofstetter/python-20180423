import time


# decorator    
def time_it(func):
    def instead_func():
        print('before time')
        func()
        print('after time')    
    return instead_func

def deco_bla(func):
    def instead_func():
        print('before')
        func()
        print('after')
    
    return instead_func


@time_it    
@deco_bla    
def bla():        
    print('bla')
    

#bla()    

bla()


    


