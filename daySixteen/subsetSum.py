def subsetSum(arr, target):
    res = []
    def backTrack(index, current, total):
        if total == target:
            res.append(current[:])
            return 
        
        if index == len(arr) or total > target:
            return
        
        current.append(arr[index]) # if current number included
        backTrack(index + 1, current, total + arr[index])

        current.pop()#if num excluded
        backTrack(index + 1, current, total)
    
    backTrack(0, [], 0) 
    return res



if __name__ == '__main__':
    arr = [2, 3, 5, 6, 7, 8]
    target = 10
    print(subsetSum(arr, target))