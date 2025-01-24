def min_bills(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for value in range(coin, amount + 1):
            dp[value] = min(dp[value], dp[value - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

test_cases = int(input())

for _ in range(test_cases):
    data = list(map(int, input().split()))
    amount = data[0]
    coins = data[1:]

    result = min_bills(amount, coins)
    print(result)