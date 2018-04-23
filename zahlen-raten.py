'''
zahlen raten:
+ zufallszahl zw 1-100
+ user darf 5 mal raten
+ info ob zu hoch oder zu nieder
'''
import random

random_int = random.randint(1, 100)
# 
max_number_of_tries = 5

print(random_int)
for tries in range(max_number_of_tries):
    print(tries)    
    try:
        user_input = input("Bitte Zahl eingeben: ")
        user_input = int(user_input)    
    except ValueError:
        print(user_input, "ist keine Zahl")
        continue

    if user_input == zufallszahl:
        print("Gewonnen!")
        break
    elif user_input > zufallszahl:
        print("zu hoch")
    else:
        print("zu niedrig")
else:
    print("leider nix. zu raten war", zufallszahl)        
    
    
        