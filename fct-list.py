def sum_list(feld):
    feld.append(4)
    sum = 0
    for a in feld:
        sum += a
    return sum
    
    
feld_main = [1,2,3]
summe = sum_list(feld_main)    
print(summe)
print(feld_main)
