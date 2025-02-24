def knapsack(max_weight, weights, values, n):
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][max_weight]

num_products = int(input())

prices = []
weights = []

for _ in range(num_products):
    price, weight = map(int, input().split())
    prices.append(price)
    weights.append(weight)

num_family_members = int(input())

max_weights = [int(input()) for _ in range(num_family_members)]

total_max_purchase = 0
for max_weight in max_weights:
    total_max_purchase += knapsack(max_weight, weights, prices, num_products)

print(total_max_purchase)