def recurse(coins, target, n):
    # print(f'computing for target: {target} and n: {n}')
    # base case
    if target <= 0:
        # return no coins i.e one way = dont return/select any coins
        # print('returning 1')
        return 1 
    
    if n == 0:
        # print('returning 0')
        # no coins, cannot make a selection unless target is also zero(=1 for this)
        return 0
    
    # inductive case for some subproblem . choice diagram
    if coins[n-1] <= target:
        val = recurse(coins, target-coins[n-1], n) + recurse(coins, target, n-1)
        # print(f'returning for {target}: {val}')
        return val
    else:
        return recurse(coins, target, n-1)

def memoized_recurse(coins, target, n):
    # check if value already computed, and return if yes
    if memoize[n][target] != -1:
        return memoize[n][target]
    
    # base case
    if target == 0:
        memoize[n][target] = 1
        return 1
    if n == 0:
        memoize[n][target] = 0
        return 0
    
    # inductive case for some subproblem, choice diagram
    if coins[n-1]  <= target:
        opt = memoized_recurse(coins, target - coins[n-1], n) + memoized_recurse(coins, target, n-1)
    else:
        opt = memoized_recurse(coins, target, n-1)
    
    # store value before returning
    memoize[n][target] = opt
    return memoize[n][target]

def top_down(coins, target, n):
    for i in range(1, n+1):
        dp[i][0] = 1
        for j in range(1,target+1):
            if coins[i-1] <= j:
                dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][target]

if __name__ == "__main__":
    coins = [1,3,5,4]
    target = 5
    n = len(coins)

    # number of ways you can get target
    ans = recurse(coins, target, n)
    print(f'naive recursion: {ans}')

    #memoization
    memoize = [[-1]*(target+1) for _  in range(n+1)]
    ans = memoized_recurse(coins, target, n)
    print(f'memoized recursion: {ans}')
    
    # # top-down approach
    dp = [[0]*(target+1) for _ in range(n+1)]
    ans = top_down(coins, target, n)
    print(f'top-down approach ans: {ans}')