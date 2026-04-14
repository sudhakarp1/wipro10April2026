'''
	strInput = '1234' base = 10
	#res = convert('123', 10)
	#res = convert('123', 8)
	#res = convert('123abc', 16)
'''
def convert(strInput, base=10):
	res = 0
	nums = ['0','1','2','3','4','5','6','7','8','9',
        'a','b','c','d','e','f' ]
	validNums = nums[:base]
	for digit in strInput:  
		if digit in validNums:
			res = res * base  + validNums.index(digit) 

	return res

res = convert('1234')
print(f'res: {res}')
res = convert('123', 10)
print(f'res: {res}')
res = convert('123', 8)
print(f'res: {res}')
res = convert('123abc', 16)
print(f'res: {res}')
