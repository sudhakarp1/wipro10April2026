from AlgorithmAnalysis import calculateTime

@calculateTime
def funAppendList(lst, num):
    for i in range(num):
        lst.append(i + 100)

@calculateTime
def funInsertList(lst, num):
    for i in range(num):
        lst.insert(0,i + 100)

if __name__ == '__main__':
    lst = []
    funInsertList(lst, 10000)
    print(lst)
