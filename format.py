a1 = int(input("Bitte Zahl eingeben: "))
a2 = int(input("Bitte Zahl eingeben: "))    

summe = a1 + a2
print("Die Summe von " + str(a1) + " und " + str(a2) + " ist " + str(summe))

# pythonic


print('Die Summe von {} und {} ist {}' \
                       .format(a1,a2,summe))

print('Die Summe von % 5u und %d ist %d' % (a1,a2,summe))
         
         