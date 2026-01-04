


number_of_days = int(input())

scores = [[] for _ in range(number_of_days)]

# [
# [], 0th list scores[0]
# [], 1st list scores[1]
# [], 2nd list
# ]
#]

#[  
# [2, 3, 8],
# [8, 2, 6],
# [6, 7, 3],
#]

for i in range(number_of_days):
    inputs = input().split()
    scores[i] = [int(x) for x in inputs]
    # equivalent to:
    # for x in inputs:
    #     scores[i].append(int(x))

# memoization is the technique to save the solutions at every stage, and use it again if needed


# [A1, B1, C1]
# [A2, B2, C2]
# [A3, B3, C3]
# ....
# [An, Bn, Cn] [n, previous_choice] # number of all possible answers is number_of_days * 3
# [An+1, Bn+1, Cn+1]
# ....

# mem = [[-1 for _ in range(3)] for _ in range(number_of_days)]
mem = []
for i in range(number_of_days):
    mem.append([-1, -1, -1])

# [
# [-1, -1, -1],
# [-1, -1, -1],
# [-1, -1, -1],
# ....
# [-1, -1, -1]
# ]

def vacation_planner(current_day, previous_choice):
    if current_day == number_of_days:
        return 0
    
    if mem[current_day][previous_choice] != -1:
        return mem[current_day][previous_choice]

    scores_current_day = scores[current_day]  # [A, B, C]

    max_score = 0

    if previous_choice != 0:
        option_a = scores_current_day[0] + vacation_planner(current_day + 1, 0)
        max_score = max(max_score, option_a)
        
    if previous_choice != 1:
        option_b = scores_current_day[1] + vacation_planner(current_day + 1, 1)
        max_score = max(max_score, option_b)

    if previous_choice != 2:
        option_c = scores_current_day[2] + vacation_planner(current_day + 1, 2)
        max_score = max(max_score, option_c)
    
    mem[current_day][previous_choice] = max_score

    return max_score


print(vacation_planner(0, -1))