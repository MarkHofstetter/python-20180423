import json, xmljson
# from lxml.etree import fromstring, tostring
import lxml.etree
from pprint import pprint

# xml = fromfile('25.04.2018_16_06_29.kml')
tree = lxml.etree.parse('25.04.2018_16_06_29.kmz')

# {http://www.opengis.net/kml/2.2}kml


ns = {'gx' : 'http://www.google.com/kml/ext/2.2'}
root = tree.getroot()
i = 0
for track in tree.findall('.//gx:Track', ns):
    # pprint(track)
    
    #for coord in track: # .findall('./gx:coord', ns):
    #    print(coord)        
    #    i += 1
    
    for i, coord in enumerate(track): # .findall('.//*gx:coord', ns):
        if i % 4 == 0:
            track.remove(coord)
        if i % 4 == 1:
            track.remove(coord)    
        print(i, coord.text)
    
    '''
    for i, speed in enumerate(track.findall('.//*gx:SimpleArrayData', ns)):
        print(i, speed.text) 
    ''' 
    
    break
 
print(i)

tree.write('out.xml') 
# print(json.dumps(xmljson.badgerfish.data(tree)))
'''

print(root)
for neighbor in root.findall('{http://www.opengis.net/kml/2.2}kml'):
    print (neighbor)
'''    