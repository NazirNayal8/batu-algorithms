import time
# 6 15
# 6 5
# 5 6
# 6 4
# 6 6
# 3 5
# 7 2

# N = 50
W = 1005

values = [5, 6, 4, 6, 5, 2, 3, 8, 3, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
weights =[6, 5, 6, 6, 3, 7, 3, 5, 2, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# W = 15
# 6 15
# 6 5
# 5 6
# 6 4
# 6 6
# 3 5
# 7 2

# weights = [6, 5, 6, 6, 3, 7]
# values = [5, 6, 4, 6, 5, 2]

N = len(values)
 
def knapsack(index, weight_left):
    if weight_left == 0:
        return 0
    if index == N:
        return 0
    
    leave_value = knapsack(index+1, weight_left)

    if weight_left-weights[index] >= 0:
        take_value = values[index] + knapsack(index+1, weight_left-weights[index])
        return max(take_value, leave_value)
    
    return leave_value

memo = [[-1 for _ in range(W+1)] for _ in range(N+1)]

def knapsack_dp(index ,weight_left):
    if weight_left == 0:
        return 0
    if index == N:
        return 0
    if memo[index][weight_left] != -1:
        return memo[index][weight_left]
    if weight_left-weights[index] >= 0:
        take_value = values[index] + knapsack_dp(index+1, weight_left-weights[index])
        leave_value = knapsack_dp(index+1, weight_left)
        memo[index][weight_left] = max(take_value, leave_value)
        return memo[index][weight_left]
    memo[index][weight_left] = knapsack_dp(index+1, weight_left)
    return memo[index][weight_left]


start = time.time()
knapsack(0, W)
print("Recursion:", time.time() - start)

start = time.time()
knapsack_dp(0, W)
print("Dynamic Programming:", time.time() - start)
