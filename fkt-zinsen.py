import zinsen as zi


print(zi.laufzeit_jahre)
    
zinsen_wert = zi.zinsen(kapital = 1000, laufzeit_jahre=10, zinsatz_prozent=3)
#zinsen_wert = zinsen(1000, zinsatz_prozent = 3)
print(zinsen_wert)