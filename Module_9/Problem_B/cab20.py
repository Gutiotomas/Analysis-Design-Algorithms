def optimal_bst_cost(freqs):
    n = len(freqs)
    
    dp = [[0] * n for _ in range(n)]
    freq_sum = [[0] * n for _ in range(n)]
    
    for i in range(n):
        freq_sum[i][i] = freqs[i]
        for j in range(i + 1, n):
            freq_sum[i][j] = freq_sum[i][j - 1] + freqs[j]
    
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            for r in range(i, j + 1):
                left_cost = dp[i][r - 1] if r > i else 0
                right_cost = dp[r + 1][j] if r < j else 0
                cost = left_cost + right_cost + freq_sum[i][j]
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1] if n > 0 else 0

def process_cases(cases):
    results = []
    for freqs in cases:
        result = optimal_bst_cost(freqs)
        results.append(result)
    return results

C = int(input())

cases = []
for _ in range(C):
    freqs = list(map(int, input().split()))
    cases.append(freqs)

results = process_cases(cases)

for result in results:
    print(result)
