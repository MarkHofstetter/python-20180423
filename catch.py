try:
    user_input = input("Bitte Zahl eingeben: ")
    user_input = int(user_input)
except ValueError:
    print(user_input, " ist keine Zahl")
    
print("Eingabe war", user_input)    
