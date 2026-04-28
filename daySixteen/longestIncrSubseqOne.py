'''
    Longest increasing subsequence
'''

def LongestISS(arr):
    size = len(arr)
    dp = [1] * size
    for i in range(size):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

if __name__ == '__main__':
    arr = [10, 9, 2, 5, 3, 7, 101, 18]

    print(f'LongestISS: {LongestISS(arr)}')

