


def minCostClimbingStairs(cost) -> int:
    n = len(cost)
    memo = [-1] * (n + 1)
    def solution(n):
        if n <= 1:
            return 0
        if memo[n] != -1:
            return memo[n]
        prev_cost = solution(n - 1) + cost[n - 1]
        prev_prev_cost = solution(n - 2) + cost[n - 2]
        memo[n] = min(prev_cost, prev_prev_cost)
        return memo[n]
    return solution(n)
    
print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
            
# 1,100,1,1,1,100,1,1,100,1 
# 0, 1 ,2,3,4, 5, 6,7, 8, 9 

# solution(10) = min(1 + solution(9), 100 + solution(8))
# solution(9) = min(100 + solution(8), 1 + solution(7))
# solution(8) = min(1 + solution(7), 1 + solution(6))
# solution(7) = min(1 + solution(6), 100 + solution(5))
# solution(6) = min(100 + solution(5), 1 + solution(4))
# solution(5) = min(1 + solution(4), 1 + solution(3))
# solution(4) = min(1 + solution(3), 1 + solution(2))
# solution(3) = min(1 + solution(2), 100 + solution(1))
# solution(2) = min(100 + solution(1), 1 + solution(0))
# solution(1) = min(1 + solution(0), cost[-1] + solution(-1))
# solution(0) = min(cost[-1] + solution(-1), cost[-2] + solution(-2)) = 1