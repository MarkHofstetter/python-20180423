import plz 

def test_valid_plz():
    test_dict = {
         'A-1234':  True,
         '1234A':   False,
         'a1234':   True,         
         'a12345454':  False, 
         'A 8782':  True,
         'Aa 1234': False,
         'b 1234':  False,
         'D-12343': False,
         'asdsad':  False,       
         123:       False,
         None:      False,
         '':        False, 
         '1234':    False,
    }

    for test_plz, ret in test_dict.items():
        ##print("{:12s}: {:6s}: {:6s}"
        ##  .format(str(test_plz), str(plz.validate(test_plz)), str(ret))) 
        assert plz.validate(test_plz) == ret    
            
    assert plz.validate([1,2]) == False
    assert plz.validate() == False
    assert plz.validate(None) == False