
N = 10

leaders = [i for i in range(N)]# [0, 1, 2, 3, 4, 5, 6, ... , N-1]
rank = [1 for _ in range(N)]

def unite(x, y): # complexity of unite is O(N) for worst case, but it is amortized O(alpha(N)) 
    leader_x = find(x)
    leader_y = find(y)

    if leader_x == leader_y:
        print("Already united")
        return
    
    if rank[leader_x] < rank[leader_y]:
        leaders[leader_x] = leader_y
    elif rank[leader_x] > rank[leader_y]:
        leaders[leader_y] = leader_x
    else:
        rank[leader_x] += 1
        leaders[leader_y] = leader_x
    

    leaders[leader_y] = leader_x


def find(x): # complexity of find is O(N) for worst case, but it is amortized O(alpha(N))
    
    while leaders[x] != x:
        leaders[x] = leaders[leaders[x]]
        x = leaders[x]
    
    return x


# NOTE: alpha(N) is the inverse Ackermann function, which grows very slowly. For all practical values of N, alpha(N) <= 4