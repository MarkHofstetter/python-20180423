'''
6 aus 45 
+ 6 nicht doppelte werte aus der zahlenmenge 1-45

+ die 6 richtigen vom mittwoch
'''

import random

all_numbers = list(range(1,46))

lotto = []
# oder lotto = list()

for _ in range(6):
    index = random.randint(0, len(all_numbers)-1)
    print(index)
    lotto.append(all_numbers[index])
    del(all_numbers[index])

lotto.sort()    
print(lotto)

print(random.sample(range(1,46),6))


lotto = []
while len(lotto) < 6:
    index = random.randint(1, 45)
    if index not in lotto:
        lotto.append(index)

print(lotto)        
        

