def optimalBST(keys, freq):
    size = len(keys)
    dp = [[0] * size for _ in range(size)]

    #cost of single key 
    for i in range(size):
        dp[i][i] = freq[i]

    for length in range(2, size + 1):
        for i in range(size - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            total = sum(freq[i: j+1])
            for r in range(i, j+1):
                left = dp[i][r-1] if r > i else 0
                right = dp[r+1][j] if r < j else 0
                dp[i][j] = min(dp[i][j], left + right + total)

    return dp[0][size - 1]

if __name__ == '__main__':
    keys, freq = [10,20,30], [3,2,4]
    #keys, freq = [10,12], [34,50]
    print(optimalBST(keys, freq))