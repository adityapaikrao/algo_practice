def top_down_dp(arr, target, n):
    if sum(arr) % 2 != 0:
        return False

    for i in range(1, n+1):
        for j in range(1, target+1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i-1][j-arr[i-1]] or dp[i-1][j])

    return dp[n][target]


if __name__ == "__main__":
    arr = [1, 5, 11, 5, 0, 2]
    n = len(arr)

    # find if arr can be divided into two sets s1 & s2 such that sum(s1) = sum(s2)

    s = sum(arr)
    # problem equivalent to finding if there is a subset with sum s/2
    target = s//2

    # top-down dp approach, initialise with base condition
    dp = [[-1]*(target+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(target+1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True

    ans = top_down_dp(arr, target, n)
    print(ans)