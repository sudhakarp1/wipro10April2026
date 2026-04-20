'''
    Extracting parts in a group
'''
import re 

print(f'finditer--> ')
pat, text = r'(\d{2})-(\d{2})-(\d{4})', 'today is 18-04-2026 and tomorrow is 19-04-2026'
res = re.search(pat, text)
print(f'\tres: {res}')
print(f'\tres: {res.groups()}')
print(f'\tres: {res.group(0)}')
print(f'\tres: {res.group(1)}')
print(f'\tres: {res.group(2)}')
print(f'\tres: {res.group(3)}')
