'''
+ usereingabe eines wortes (deutsch oder englisch!!)
+ ausgabe der überstzung so vorhanden

+ testbarkeit im blick haben, dh zumindst das übersetzen in eine function auslagern

eingabe: maus => mouse
         mouse => maus
'''
def main():
    import configparser
    from pprint import pprint

    config = configparser.ConfigParser()
    config.read('dictionary.ini')
    config.sections()

    eng2ger = dict(config['english_to_german'])
        
    user_word = input('Wort eingeben: ')        
    try:
        translated = translate(user_word, eng2ger)
        print(translated)
    except ValueError:
        print("wort unbekannt")

               
def translate(user_word, eng2ger):
    #ger2eng = dict((v,k) for k,v in eng2ger.items())    
    ger2eng = dict( zip(eng2ger.values(), eng2ger.keys()) )

    translation = None
    if user_word in eng2ger:
        translation = eng2ger[user_word]
    elif user_word in ger2eng:
        translation = ger2eng[user_word]
    else:
        raise ValueError('word not found')
    return translation


if __name__ == '__main__':
    main()

    

    





