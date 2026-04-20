'''

'''
import re 

pat, text = r'\d+', 'Checking 12334 with number here 934875935'
res = re.search(pat, text)
print(f'res: {res}')
print(f'finditer--> ')
pat, text = r'\d+', 'Checking 12334 with number here 934875935 and 234'
res = re.finditer(pat, text)
for each in res:
    print(f'\t\tres: {each.group()}, {each.span()}')
