def max_score(spaces):
    if len(spaces) == 0:
        return 0
    elif len(spaces) == 1:
        return spaces[0]
    
    dp = [0] * len(spaces)
    
    dp[0] = spaces[0]
    if len(spaces) > 1:
        dp[1] = max(spaces[0], spaces[1])
    
    for i in range(2, len(spaces)):
        dp[i] = max(dp[i-1], dp[i-2] + spaces[i])
    
    return dp[-1]

t = int(input())
for _ in range(t):
    n = int(input())
    spaces = []
    for _ in range(n):
        spaces.append(int(input()))
    
    print(max_score(spaces))