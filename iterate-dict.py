participents = {
    'Martin':     {'year': 1976, 'height': 180, 'education': ['VS', 'Gym', 'Uni']},
    'Harald':     1970,
    'Gerald':     1973,
    'RolandW':     1998,
    'Christoph':  1981,
    'RolandS':     {'year': 1974, 'education': ['VS', 'Gym', 'Uni']},
}

for name in participents:
    print(participents[name])

for name, data in participents.items():
    print(name, data)
    