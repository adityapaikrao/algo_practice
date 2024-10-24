def recurse(coins, target):
    # base case
    if len(coins) == 0 or target == 0:
        return 0
    
    # inductive case for some sub-problem / choice diagram
    opt = float('inf')
    for coin in coins:
        if coin <= target:
            opt = min(opt, 1 + recurse(coins, target-coin))
    return opt

def memoized_recurse(coins, target):
    # base case
    if len(coins) == 0 or target <= 0:
        memoize[target] = 0
        return memoize[target]
    
    # check if already computed
    if memoize[target] != -1:
        return memoize[target]
    
    # inductive case for some subproblem / choice diagram
    opt = float('inf')
    for coin in coins:
        if coin <= target:
            # store the value when subproblem is getting computed
            opt = min(opt, 1 + memoized_recurse(coins, target-coin))
    memoize[target] = opt
    return memoize[target]

def top_down(coins, target):
    for i in range(1, target+1):
        dp[i] = float('inf')
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i-coin] + 1, dp[i])
    return dp[target]
if __name__ == "__main__":
    coins = [1, 2, 3]
    target = 12

    # min number of coins to get target
    ans = recurse(coins, target)
    print(f'naive recursion: {ans}')

    # #memoization
    memoize = [-1 for _  in range(target+1)]
    ans = memoized_recurse(coins, target)
    print(f'memoized recursion: {ans}')
    
    # top-down approach
    dp = [0 for _ in range(target+1)]
    ans = top_down(coins, target)
    print(f'top-down approach ans: {ans}')