def recursive_sol(w, v, max_w, n):
    # base condition: think of smallest valid input
    if n == 0 or max_w == 0:  # when no capacity of knapsack or no items
        return 0
    # choice diagram: recursion always call on a smaller input n -> n-k
    if w[n - 1] > max_w:
        return recursive_sol(w, v, max_w, n - 1)
    elif w[n - 1] <= max_w:
        return max(recursive_sol(w, v, max_w, n - 1), v[n - 1] + recursive_sol(w, v, max_w - w[n - 1], n - 1))


def recursive_memoized(w, v, max_w, n):
    # base condition
    if n == 0 or max_w == 0:
        return 0
    # add memoization check
    if memoize[n][max_w] != -1:
        return memoize[n][max_w]

    # choice diagram
    if w[n - 1] > max_w:
        memoize[n][max_w] = recursive_memoized(w, v, max_w, n - 1)
        return memoize[n][max_w]
    elif w[n - 1] <= max_w:
        memoize[n][max_w] = max(v[n - 1] + recursive_memoized(w, v, max_w - w[n - 1], n - 1),
                                recursive_memoized(w, v, max_w, n - 1))
        return memoize[n][max_w]


def top_down_dp(w, v, max_w, n):
    # same complexity as memoized version. can be used to avoid stack overflow from recursive call
    for i in range(1, n+1):
        for j in range(1, max_w+1):
            if w[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(v[i-1]+dp[i-1][j-w[i-1]], dp[i-1][j])
    return dp[n][max_w]


if __name__ == "__main__":
    w = [1, 3, 4, 5]
    v = [1, 4, 5, 7]
    max_w = 7
    n = len(w)

    # recursion
    max_profit = recursive_sol(w, v, max_w, n)
    print(max_profit)

    memoize = [[-1] * (max_w + 1) for _ in range(n + 1)]
    print(len(memoize), len(memoize[0]))

    # recursion with memoization
    max_profit = recursive_memoized(w, v, max_w, n)
    print(max_profit)

    # recursion with top-down approach
    dp = [[0]*(max_w+1) for _ in range(n+1)] # intialize for base condition
    max_profit = top_down_dp(w, v, max_w, n)
    print(max_profit)