def fun(num):
    if num <= 10:
        print(num, end=' ')
        funOne(num + 1)

def funOne(num):
    if num <= 10:
        print(num, end=' ')
        fun(num + 1)
        
fun(1)