import re 
#match() matches only at the begining of string
text, pat = 'Hello how are you', 'how'
res = re.search(pat, text) 
print(f'res.group(): {res.group()}')
print(f'res.span(): {res.span()}')
print(f'res.start(): {res.start()}')
print(f'res.end(): {res.end()}')
print(f'matched pattern: {text[res.start(): res.end()]}')

'''
if res:
    print('Match Found')
else:
    print('Match NOT Found')
'''
#print(f'res.groups(): {res.groups()}')