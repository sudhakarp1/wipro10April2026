def fun(num):#direct recursive function
    if num<=10:
        print(num, end=' ')
        fun(num+1)


fun(1)