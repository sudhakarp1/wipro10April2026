def linearSearch(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

def binarySearch(lst, target):
    left, right = 0, len(lst) - 1
    
    while left <= right:
        mid = (left + right) // 2
        #print(f'{lst[mid]}  {target} --> Mid: {mid}  L: {left} --> R: {right}')

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:            
            right = mid - 1

    return -1

from math import sqrt 

def jumpSearch(lst, target):
    size = len(lst)
    step, prev= int(sqrt(size)), 0

    while prev < size and lst[min(step, size)-1] < target:
        prev = step 
        step += int(sqrt(size))
        if prev >= size:
            return -1
    #linear search 
    for index in range(prev, min(step, size)):
        if lst[index] == target:
            return index
    return -1

if __name__ == '__main__':
    myList = [33,97,66,21,22,11,87,56]
    myList.sort()
    print(f'myList: {myList} ')
    print(f'{jumpSearch(myList,11)}')
    print(f'{jumpSearch(myList,97)}')
    print(f'{jumpSearch(myList,22)}')
    print(f'{jumpSearch(myList,101)}')