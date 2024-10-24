def recurse(arr, target, n):
    # base condition, if no element & target != 0 we cant get subset,
    # else if target == 0 we can always get an empty set
    if target == 0:
        return True
    elif n == 0:
        return False

    # choice diagram: for each element we can choose if it is in the subset or not
    if arr[n - 1] > target:
        return recurse(arr, target, n - 1)
    else:
        # not in subset
        c1 = recurse(arr, target, n - 1)
        # in subset
        c2 = recurse(arr, target - arr[n - 1], n - 1)
        return (c1 or c2)


def recurse_memoized(arr, target, n):
    # base condition
    if target == 0:
        mem[n][target] = True
    elif n == 0:
        mem[n][target] = False

    # check if already memoized
    if mem[n][target] != -1:
        # print("memoized for: n {}, target {}".format(n, target))
        return mem[n][target]

    # memoize and recurse
    # print("checking for n: {}, target: {}".format(n, target))
    if arr[n - 1] > target:
        mem[n][target] = recurse_memoized(arr, target, n - 1)
    else:
        c1 = recurse_memoized(arr, target - arr[n - 1], n - 1)
        c2 = recurse_memoized(arr, target, n - 1)
        mem[n][target] = (c1 or c2)

    return mem[n][target]



def top_down_dp(arr, target, n):
    for i in range(1, n+1):
        for j in range(1, target+1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i-1][j] or dp[i-1][j-arr[i-1]])

    return dp[n][target]


if __name__ == "__main__":
    arr = [2, 3, 7, 2, 10]
    target = 11
    n = len(arr)

    # find if there is a subset with sum of elements = target

    # try recursion first
    ans = recurse(arr, target, n)
    print(ans)

    # memoize it
    mem = [[-1] * (target + 1) for _ in range(n + 1)]
    ans = recurse_memoized(arr, target, n)
    print(ans)
    print(mem)

    # top down approach
    dp = [[-1]*(target+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(target+1):
            print(i, j)
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True

    ans = top_down_dp(arr, target, n)
    print(ans)
