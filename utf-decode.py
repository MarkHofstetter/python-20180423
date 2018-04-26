from pprint import pprint
text = 'öö€€€'

print(type(text))

text2 = bytes(text, 'utf-8')

bla = bytearray(text2)

pprint(bla)

print(len(text), len(text2))
print(type(text2))

print(text)