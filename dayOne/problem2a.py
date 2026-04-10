'''
    Purpose:
    Using  bitwise operators 
	a. Check whether given bit position in a number is ON or OFF
		for example:
		------------
			num = 10, pos = 1
			Bit representation -->  1010 
									0010  AND
								------------
									0010  --> Non Zero --> ON 
								------------ 
											if Zero --> OFF
'''

num, pos = 10, 2

res = 'ON' if num & 1 << pos else 'OFF'
print(f'{pos} bit on num {num} is {res}')

