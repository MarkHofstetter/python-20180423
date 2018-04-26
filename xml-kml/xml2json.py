import json, xmljson
# from lxml.etree import fromstring, tostring
import lxml.etree
from pprint import pprint

# xml = fromfile('25.04.2018_16_06_29.kml')
tree = lxml.etree.parse('25.04.2018_16_06_29.kml')

# {http://www.opengis.net/kml/2.2}kml


ns = {'gx' : 'http://www.google.com/kml/ext/2.2'}
root = tree.getroot()
for coord in tree.findall('.//*gx:coord', ns):
    print(coord.text)
 
# print(json.dumps(xmljson.badgerfish.data(tree)))
'''

print(root)
for neighbor in root.findall('{http://www.opengis.net/kml/2.2}kml'):
    print (neighbor)
'''    