'''
    user raising exception
'''

def convert(strInput, base=10):
	res = 0
	nums = ['0','1','2','3','4','5','6','7','8','9',
        'a','b','c','d','e','f' ]
	validNums = nums[:base]
	try:
		for digit in strInput:  
			if digit in validNums:
				res = res * base  + validNums.index(digit) 
			else:
				res=0
				raise ValueError(f'Invalid literal {strInput}-->{digit}')
	except ValueError as ve:
		print(ve)		
	return res

if __name__ =='__main__':
	print(f"123abc, 16--> {convert('123abc', 16)}")
	print(f"'123ab', 12-->  {convert('123ab', 12)}")
	print(f"'123abcf', 12--> {convert('123abcf', 12)}")
	print(f"'100234' -->  {convert('100234')}")
	