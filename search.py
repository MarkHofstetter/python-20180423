text = 'die ist mein zu durchsuchender Text'
print(text)

searchstring = input("Suchtext eingeben bitte: ")
if searchstring.strip().lower() in text.lower():
    print(searchstring, "enthalten")
else:
    print(searchstring, "nicht gefunden")
