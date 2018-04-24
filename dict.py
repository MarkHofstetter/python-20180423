import pprint

#    key          value
#    schlüssel    werte
teilnehmer = {
    'Martin':     {'year': 1976, 'height': 180, 'education': ['VS', 'Gym', 'Uni']},
    'Harald':     1970,
    'Gerald':     1973,
    'RolandW':     1998,
    'Christoph':  1981,
    'RolandS':     1974,
}

teilnehmer['Mark'] = 1975
print(teilnehmer['Martin'])
## pprint.pprint(teilnehmer)
