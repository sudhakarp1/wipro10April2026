'''
    strInput = '1234' base = 10
    '1' 
    #res = convert('123', 10)
    #res = convert('123', 8)
    #res = convert('123abc', 16)
'''

def convert(strInput, base):
    res = 0
    for digit in strInput:  
        res = res * base  + (ord(digit) - ord('0')) 
    return res

res = convert('1234', 10)
print(f'res: {res}')

