def lcs(s1, s2):
    len1, len2 = len(s1), len(s2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len1][len2]

def plan_trips(pairs):
    results = []
    for s1, s2 in pairs:
        lcs_length = lcs(s1, s2)
        results.append(lcs_length)
    return results

S = int(input())
pairs = []

for _ in range(S):
    s1, s2 = input().split()
    pairs.append((s1, s2))

results = plan_trips(pairs)

for result in results:
    print(result)
