print("zinsen modul")

laufzeit_jahre = 12

def zinsen(kapital, laufzeit_jahre=10, zinsatz_prozent=3):
    return kapital * (1 + zinsatz_prozent/100)**laufzeit_jahre