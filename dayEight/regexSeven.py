import re 
text = 'Checking 12334   with number   here 934875935 and 234'
res = re.sub(r"\d+", 'XXXXX',text) #pat,repl, text
print(f'res: {res}')

res = re.sub(r"\s", '*',text) #pat,repl, text
print(f'res: {res}')

res = re.split(r"\s+", text) #pat,repl, text
print(f'res: {res}')