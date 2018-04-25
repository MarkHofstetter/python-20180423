import re

'''
returns True/False

1. a oder A 
2. nichts oder Leerzeichen oder -
3. 4 Ziffern

'''

plzre = re.compile(r'^[Aa][- ]{0,1}(\d{4})$')

def validate(plz = None):
    plz = str(plz)
    matches = plzre.search(plz)
    if matches:
        print(matches.group(1))
        return True
    else:
        return False
