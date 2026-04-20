'''
    Extracting parts in a group
            --> named group
'''
import re 

print(f'finditer--> ')
pat, text = r'(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})', 'today is 18-04-2026 and tomorrow is 19-04-2026'
res = re.search(pat, text)
print(f'\tres: {res}')
print(f'\tres: {res.groups()}')
print(f'\tres: {res.group(0)}')
print(f'\tres: {res.group('day')}')
print(f'\tres: {res.group('month')}')
print(f'\tres: {res.group('year')}')
