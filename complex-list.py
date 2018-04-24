'''
+ eingabe eines names durch den user
+ dann ausgabe der letzten Ausbildung (so vorhanden)

zb 
Eingabe: Martin
Ausgabe: Uni

Eingabe: Ivan
Ausgabe: n/a

+ zusatz: den ältesten/jüngsten aus der liste
'''

import pprint

participents = [
    ['Martin',    1976, ['VS', 'Gym', 'Uni']],
    ['Harald',    1970],
    ['Eva',       1973],
    ['Roland',    1998],
    ['Christoph', 1981],
    ['Roland',    1974],
    ['Reza',      1994, ['Informatik']],
    ['Ivan',      1985],
    ['Daniel',    1990],
    ['Reinhard',  1987],
    ['Alexander', 1986],
    ['Mark',      1975],       
]

participents.append(['Michala', 1975, ['VS', 'Gym', 'Uni']])
participents.sort()


# participents.sort(key=lambda p: p[1])
pprint.pprint(participents)

n, y = zip(*participents)

print(y)

exit()

years_of_birth = [p[1] for p in participents]
names          = [p[0] for p in participents]



pprint.pprint(years_of_birth)

min_year = min(years_of_birth)
print(min_year)

index = years_of_birth.index(min_year)
print(index)
print(participents[index])
exit()

name = input('Namen eingeben: ')


for participent in participents:
    if name == participent[0]:
        try:
            print(participent[2][-1])
        except IndexError:
            print('n/a')