a1 = int(input("Bitte Zahl eingeben: "))
a2 = int(input("Bitte Zahl eingeben: "))    

summe = a1 + a2
print("Die Summe von " + str(a1) + " und " + str(a2) + " ist " + str(summe))

# pythonic
formatted_result = 'Die Summe von {} und {} ist {}' \
                       .format(a1,a2,summe)

print(formatted_result)

print('Die Summe von % 5u und %d ist %d' % (a1,a2,summe))
         
         