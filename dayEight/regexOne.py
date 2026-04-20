'''
    Intro to regular expression module
    match(), search()    
'''

import re 
#match() matches only at the begining of string
res = re.match('Hello','Hello how are you') 
print(f'res: {res}')
res = re.match('how','Hello how are you')
print(f'res: {res}')

#search() finds the first match anywhere in the string
res = re.search('how','Hello how are you')
print(f'res: {res}')

