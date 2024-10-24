def recurse(prices, n):
    # base case when rod length is 1
    if n == 1:
        return prices[n-1] 
    # for inductive case i aka choice diagram for case i
    opt = float('-inf')
    for i in range(1, n):
        opt = max(opt, prices[i-1] + recurse(prices, n-i))
    return opt

def memoized_recurse(prices, n):
    if n==1:
        return prices[n-1]
    
    # if already computed return it
    if memoize[n] != -1:
        return memoize[n]
    
    # inductive case
    opt  = float('-inf')
    for i in range(1, n):
        val = memoized_recurse(prices, n-i)
        # store value when computing
        memoize[n-i] = val
        opt = max(opt, prices[i-1] + val)
    memoize[n] = opt
    return memoize[n]

def top_down(prices, n):
    for i in range(1, n+1):
        for j in range(i):
            dp[i] = max(prices[j] + dp[i-j], dp[i-1])
        print(f'after {i} :', dp)
    return dp[n]
if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10]
    n = len(prices)

    # maximise profit by cutting rod
    ans = recurse(prices, n)
    print(f'naive recursion: {ans}')

    #memoization
    memoize = [-1 for _  in range(n+1)]
    ans = memoized_recurse(prices, n)
    print(f'memoized recursion: {ans}')
    
    # top-down approach
    dp = [0 for _ in range(n+1)]
    ans = top_down(prices, n)
    print(f'top-down approach ans: {ans}')