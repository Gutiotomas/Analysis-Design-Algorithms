from itertools import permutations

def calculate_min_cost(dist_matrix, cities):
    n = len(cities)
    min_cost = float('inf')
    
    for perm in permutations(cities):
        total_cost = 0
        valid_route = True
        
        for i in range(n - 1):
            cost = dist_matrix[perm[i]][perm[i+1]]
            if cost == float('inf'):
                valid_route = False
                break
            total_cost += cost
                   
        if valid_route:
            min_cost = min(min_cost, total_cost)

    return min_cost if min_cost != float('inf') else "imposible"


cases = int(input())
for _ in range(cases):
    cities = int(input())
    dist_matrix = []
    
    for i in range(cities):
        row = input().split()
        dist_matrix.append([
            float(val) if val != 'n.a' else float('inf') for val in row
        ])
    
    cities = list(range(cities))
    
    result = calculate_min_cost(dist_matrix, cities)
    
    if isinstance(result, float):
        print(int(round(result / 10)))
    else:
        print(result)