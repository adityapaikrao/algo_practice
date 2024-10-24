def top_down_dp(arr, target, n):
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
                # total subsets =  subsets including + subsets excluding

    return dp[n][target]


if __name__ == "__main__":
    arr = [2, 3, 5, 6, 8, 10]
    target = 10
    n = len(arr)

    # count number of subsets with sum = 10
    # top-down dp approach
    dp = [[-1] * (target + 1) for _ in range(n+1)]

    # initialise dp matrix
    for i in range(n + 1):
        for j in range(target + 1):
            if i == 0:
                dp[i][j] = 0
            if j == 0:
                dp[i][j] = 1

    ans = top_down_dp(arr, target, n)
    print(ans)
