'''
    findall() -->returns list of matched patterns --> 
'''
import re 
pat, text = r'\d+', 'Checking 12334 with number here 934875935 and 234'
res = re.findall(pat, text)
print(f'res: {res}')
