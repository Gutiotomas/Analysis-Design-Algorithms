MOD = 999999937

def precompute_max_values(max_height):
    max_values = [0] * (max_height + 1)
    triangle = [[0] * (h + 1) for h in range(max_height + 1)]
    
    for h in range(max_height + 1):
        triangle[h][0] = triangle[h][h] = 1
        max_in_row = 1
        
        for k in range(1, h):
            triangle[h][k] = triangle[h - 1][k - 1] + triangle[h - 1][k]
            max_in_row = max(max_in_row, triangle[h][k])
        
        max_values[h] = max_in_row
    
    return max_values

def solve_triangle(test_cases):
    max_height = max(test_cases)
    max_values = precompute_max_values(max_height)
    
    results = []
    for h in test_cases:
        results.append(max_values[h - 1] % MOD)
    return results

num_cases = int(input())
test_cases = [int(input()) for _ in range(num_cases)]

results = solve_triangle(test_cases)

for result in results:
    print(result)