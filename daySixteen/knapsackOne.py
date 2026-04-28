
def knapsack(weights, values, capacity):
    size = len(weights)
    dp = [ [0] * (capacity + 1) for _ in range(size + 1)] 
    for i in range(1, size + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], 
                               values[i-1] + dp[i-1][w-weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]    
    
    return dp[i][capacity]


if __name__ == '__main__':
    wt = [1,2,4,5]
    val = [1,4,5,7]
    W = 7
    res = knapsack(wt, val, W)
    print(f'Total: {res}')
    '''
    for row in res:
        print(*row)
    
    print(f'Total: {res[len(wt)][W]}')
    '''
