num_cases = int(input())

for _ in range(num_cases):
    data = list(map(int, input().split()))
    num_candies = data[0]
    candy_prices = data[1:]
    
    min_cost = [float('inf')] * (num_candies + 1)
    max_cost = [0] * (num_candies + 1)
    
    for i in range(1, num_candies + 1):
        min_cost[i] = candy_prices[i - 1]
        max_cost[i] = candy_prices[i - 1]
    
    for i in range(2, num_candies + 1):
        for j in range(1, i):
            min_cost[i] = min(min_cost[i], min_cost[j] + min_cost[i - j])
            max_cost[i] = max(max_cost[i], max_cost[j] + max_cost[i - j])
    
    print(min_cost[num_candies], max_cost[num_candies])