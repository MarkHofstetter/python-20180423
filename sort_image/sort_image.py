'''
+ quell und zielverzeichnis auf einer config 
+ verzeichnis rekrusiv durchsuchen
+ a/b/c/diese datei.jfif => a_b_c_diese_datei.jfif
+ ...
+ testbar

spaces mit underscore ersetzen 

+ zusatzaufgabe bilder resizen auf max_length 100

'''

import os, shutil
import re

def flatten_dir(source_dir, target_dir):
    if not os.path.isdir(target_dir):
        os.mkdir(target_dir)
    for root, dirs, files in os.walk(source_dir):
        for file in files:        
            new_filename = re.sub(r'\s+', r'_', file)            
            path = root.split(os.sep)[1:]
            new_filename = '_'.join(path) + '_' + new_filename   
            fullname = os.path.join(target_dir, new_filename)
            if os.path.isfile(fullname):
                exit('uiuiui')            
            shutil.copy(os.path.join(root, file), 
                        fullname)





