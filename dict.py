import pprint

'''
+ eingabe eines names durch den user
+ dann ausgabe der letzten Ausbildung (so vorhanden)

zb 
Eingabe: Martin
Ausgabe: Uni
'''

#    key          value
#    schlüssel    werte
teilnehmer = {
    'Martin':     {'year': 1976, 'height': 180, 'education': ['VS', 'Gym', 'Uni']},
    'Harald':     1970,
    'Gerald':     1973,
    'RolandW':     1998,
    'Christoph':  1981,
    'RolandS':     {'year': 1974, 'education': ['VS', 'Gym', 'Uni']},
}

teilnehmer['Mark'] = 1975

## pprint.pprint(teilnehmer)

name = input('Namen eingeben: ')
'''
try:
    print(teilnehmer[name])
except KeyError:
    print('teilnehmer nicht gefunden')
'''
if name in teilnehmer:
    print(teilnehmer[name])
    if type(teilnehmer[name]) is dict:
        print(teilnehmer[name]['education'][-1])
    else:
        print('n/a')
else:
    print('teilnehmer nicht gefunden')    

