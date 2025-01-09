def minCostClimbingStairs(cost) -> int:
    n = len(cost)
    def solution(n):
        if n == -1:
            return 0
        return min(solution(n-1), solution(n-2))
    
    return solution(n)
    

print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
            

        
