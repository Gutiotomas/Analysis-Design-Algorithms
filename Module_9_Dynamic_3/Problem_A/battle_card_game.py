def divisors_count(S):
    count = 0
    for i in range(1, int(S**0.5) + 1):
        if S % i == 0:
            count += 1
            if i != S // i:
                count += 1
    return count

def fuse_cards(cards):
    n = len(cards)
    dp = [[0] * n for _ in range(n)]
    max_id = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = cards[i][1]
        max_id[i][i] = cards[i][0]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                left = dp[i][k]
                right = dp[k+1][j]
                fusion_sum = left + right
                fusion_divisors = divisors_count(fusion_sum)
                new_power = fusion_sum + fusion_divisors
                new_id = max(max_id[i][k], max_id[k+1][j])

                if dp[i][j] < new_power:
                    dp[i][j] = new_power
                    max_id[i][j] = new_id

    return dp[0][n-1]

test_cases = int(input())
for _ in range(test_cases):
    num_cards = int(input())
    cards = []
    for _ in range(num_cards):
        id, power = map(int, input().split())
        cards.append((id, power))
    cards.sort()
    if num_cards == 1:
        print(cards[0][1])
    else:
        result = fuse_cards(cards)
        print(result)