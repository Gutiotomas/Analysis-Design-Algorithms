denominations = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

cases = int(input())

for _ in range(cases):
    value = int(input())
    total_coins = 0

    for d in denominations:
        if value >= d:
            total_coins += value // d
            value = value % d

    print(total_coins)