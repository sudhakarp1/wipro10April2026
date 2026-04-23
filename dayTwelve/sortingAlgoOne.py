'''
    Sorting algorithms
        Bubble Sort (Strategy: Exchanging)
        Quick Sort (Strategy: Divide and Conquer)
        Merge Sort (Strategy: Divide and Conquer)
        Heap Sort (Strategy: Selection)
'''

def bubbleSort(lst):
    size = len(lst)
    for i in range(size):
        isSwapped = False
        for j in range(0, size - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                isSwapped = True
        if not isSwapped:
            break 

def quickSort(lst):
    if len(lst) <= 1:
        return lst 
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    return quickSort(left) + middle + quickSort(right)

def mergeSort(lst):
    if len(lst) <= 1:
        return lst 
    mid = len(lst) // 2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])

    return mergeList(left, right)

def mergeList(leftLst, rightLst):
    res = []
    i = j = 0
    while i < len(leftLst) and j < len(rightLst):
        if leftLst[i] < rightLst[j]:
            res.append(leftLst[i])
            i += 1
        else:
            res.append(rightLst[j])
            j += 1
    
    res.extend(leftLst[i:]) 
    res.extend(rightLst[j:]) 
    return res 

def heapSort(lst):
    size = len(lst) 

    for index in range(size // 2 - 1, -1, -1):#build max heap
        heapify(lst, size, index)


    for index in range(size - 1, 0, -1):
        lst[0], lst[index] = lst[index], lst[0]
        heapify(lst, index, 0)

    return lst

def heapify(lst, size, index):#max heap
    largest = index
    leftChild = 2 * index + 1
    rightChild = 2 * index + 2

    if leftChild < size and lst[leftChild] > lst[largest]:
        largest = leftChild

    if rightChild < size and lst[rightChild] > lst[largest]:
        largest = rightChild

    if largest != index:
        lst[index], lst[largest] = lst[largest], lst[index]
        heapify(lst, size, largest)       


if __name__ == '__main__':
    from random import randint
    numValues = 10
    lstOne = [randint(1, 1000) for _ in range(numValues)]
    print(f'lst: {lstOne}')
    heapSort(lstOne)
    print(f'lst: {lstOne}')
