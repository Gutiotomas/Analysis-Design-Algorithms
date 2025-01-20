def min_difference(sets):
    results = []
    
    for coins in sets:
        total = sum(coins)
        half = total // 2
        
        dp = [False] * (half + 1)
        dp[0] = True
        
        for coin in coins:
            for j in range(half, coin - 1, -1):
                dp[j] = dp[j] or dp[j - coin]
        
        for i in range(half, -1, -1):
            if dp[i]:
                sum1 = i
                sum2 = total - sum1
                results.append(abs(sum1 - sum2))
                break
                
    return results

C = int(input())
sets = []

for _ in range(C):
    coins = list(map(int, input().split()))
    sets.append(coins)

for result in min_difference(sets):
    print(result)