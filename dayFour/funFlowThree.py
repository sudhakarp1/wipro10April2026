def fun(num):#recursive functions
    if num<=5:
        print(num, end=' ')
        fun(num+1)
        print(num, end=' ')

fun(1)