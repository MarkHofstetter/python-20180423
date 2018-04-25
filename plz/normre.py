import re

address = '   Schulg.    234;       1090    gars am kamp, Stiege 27  '
address = address.strip()
print('>'+address+'<')
address = re.sub(r'\s+', ' ', address)
# rep = '\1asse'
# reg = re.compile(re.escape(rep))
address = re.sub(r'([Gg])\.', r'\1asse', address)
print("[%s]" % (address))
