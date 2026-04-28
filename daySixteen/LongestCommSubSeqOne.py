def longestCommonSubSeq(s1, s2):
    lenStr1, lenStr2 = len(s1), len(s2)
    dp = [[0] * (lenStr2 + 1) for _ in range(lenStr1 + 1)]

    for i in range(1, lenStr1 + 1):
        for j in range(1, lenStr2 + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[i][j]

if __name__ == '__main__':
    s1, s2='LKSADFJSD', 'KKKSDALFJLS'
    print(longestCommonSubSeq(s1, s2))
