
memo = [-1] * 1000

def climbStairs(n: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0
    if memo[n] != -1:
        return memo[n]
    memo[n] = climbStairs(n-1) + climbStairs(n-2)
    return memo[n]
    
n = 900
print(climbStairs(n)) # 8