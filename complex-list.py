'''
+ eingabe eines names durch den user
+ dann ausgabe der letzten Ausbildung (so vorhanden)

zb 
Eingabe: Martin
Ausgabe: Uni

Eingabe: Ivan
Ausgabe: n/a
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

pprint.pprint(participents)


for participent in participents:
    print(participent[0])