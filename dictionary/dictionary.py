'''
+ usereingabe eines wortes (deutsch oder englisch!!)
+ ausgabe der überstzung so vorhanden

+ testbarkeit im blick haben, dh zumindst das überstzen in eine function auslagern

eingabe: maus => mouse
         mouse => maus
'''


import configparser
from pprint import pprint

config = configparser.ConfigParser()
config.read('dictionary.ini')
config.sections()

wb = config['english_to_german']
pprint(wb['house'])
print(config['english_to_german']['house'])

