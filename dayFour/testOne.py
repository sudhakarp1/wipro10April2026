'''
ch = '1'
print(f'ch: {ch}--> {ord(ch[0])}') # ASCII of '1' is 49
print(f'ch: {ch}--> {chr(49)}') #ASCII Char of 49 is '1'
'''
def generate_binary(n, s=""):
    if n == 0:
        print(s)
    else:
        generate_binary(n-1, s + "0")
        generate_binary(n-1, s + "1")

generate_binary(2)