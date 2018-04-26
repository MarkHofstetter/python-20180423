import xml.parsers.expat
import argparse
from pprint import pprint
from lxml import xml 

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--inputfile',
  action="store", dest="inputfile",
  help="inputfile to be parsed")

parser.add_argument('-d', '--debug',
  help="debug")

options = parser.parse_args()
print ('Input File', options.inputfile)

p = xml.parsers.expat.ParserCreate()

with open(options.inputfile, 'rb') as kmlfile:
    p.ParseFile(kmlfile)
    pprint(p)