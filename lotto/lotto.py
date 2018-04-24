'''
6 aus 45 
+ 6 nicht doppelte werte aus der zahlenmenge 1-45

+ die 6 richtigen vom mittwoch
'''

import random

def lotto_man():
    all_numbers = list(range(1,46))
    lotto = []
    for _ in range(6):
        index = random.randint(0, len(all_numbers)-1)        
        lotto.append(all_numbers[index])
        del(all_numbers[index])
    return lotto

def random_sample():
    return random.sample(range(1,46),6)


def lotto_man_bad():
    lotto = []
    while len(lotto) < 6:
        index = random.randint(1, 45)
        if index not in lotto:
           lotto.append(index)
    return lotto
        

