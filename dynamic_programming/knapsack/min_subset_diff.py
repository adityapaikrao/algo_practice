def recurse(arr, n, target):
    print(arr, "n: {}  target: {}".format(n, target))
    # base condition
    if target == 0:
        print("c00")
        mem[n][target] = True
        return True
    if n == 0:
        print("c01")
        mem[n][target] = False
        return False

    # check if memoized
    if mem[n][target] != -1:
        print("mem")
        return mem[n][target]

    # choose between choices
    if arr[n-1] > target:
        print("choose1")
        mem[n][target] = recurse(arr, n-1, target)
        print(mem)
        print(mem[n][target])
    else:
        print("choose2")
        k1= (recurse(arr, n-1, target-arr[n-1]))
        k2= (recurse(arr, n-1, target))
        mem[n][target] = k1 or k2
        print(mem)
        print(mem[n][target])

    return mem[n][target]


def top_down_dp(arr, n, target):
    for i in range(1, n+1):
        for j in range(1, target+1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]

    valid_sum = []
    for j in range(target+1):
        if dp[n][j]:
            valid_sum.append(j)
    return valid_sum


if __name__ == "__main__":
    arr = [1, 2, 7]
    n = len(arr)

    # find subsets s1 & s2 such that value of |s1-s2| is minimum.
    # s1 + s2 = sum(arr) -> min |s1 -s2| => min |2s1 - S| => find all s1 and minimize

    target = sum(arr)
    # memoized recursion
    mem = [[-1]*(target+1) for _ in range(n+1)]

    recurse(arr, n, target)

    # WONT WORK WITH MEMOIZATION AS YOU ARE SKIPPING FOR DIFFERENT TARGETS AT n = n_max, use top-down dp

    # top-down dp
    dp = [[-1]*(target+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(target+1):
            if i == 0:
                print("c1")
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True
    print(dp)
    valid_sum = top_down_dp(arr, n, target)

    # for valid sums find mimimum of |2s1-S|
    min_difference= float('inf')
    for s in valid_sum:
        min_difference = min(min_difference, abs(2*s -target))
    print(min_difference)
